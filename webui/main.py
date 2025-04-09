import asyncio
import re

import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from ollama import AsyncClient

import warnings

warnings.filterwarnings("ignore")
from typing import AsyncGenerator, NoReturn

from agent.graph import create_graph
from langgraph.types import Command
from langgraph.checkpoint.memory import MemorySaver

from base64 import b64encode

app = FastAPI()

with open("./webui/index.html") as f:
    html = f.read()

headers = {"Content-Type": "application/json"}
model_endpoint = "http://localhost:11435/api/generate"
temperature = 0
# model = "llama3-groq-8b-Q8:latest"
model = "gpt-4o"

memory = MemorySaver()
graph = create_graph(model=model, model_endpoint=model_endpoint)
workflow = graph.compile(checkpointer=memory)


def print_workflow(event):
    # print(event)    assert "__interrupt__" in event
    content = event["__interrupt__"][0].value

    print("Event from interrupt: ", event)

    formatted = "> Review the following:\n"
    formatted += "Agent will . . ."

    for header in content:
        tools = content[header]
        for tool in tools:
            if "tool_call" in tool and tool["tool_call"]:
                fname = tool["tool_call"]["name"]
                args = tool["tool_call"]["arguments"]
                formatted += f"{fname} with {args} ==> "
            # formatted += str(tool.values()) + "\n"
    formatted += "[x]"
    return formatted


def get_image_binary(file_path):

    with open(file_path, "rb") as image_file:
        image_data = b64encode(image_file.read()).decode("utf-8")
        return image_data


async def chat(message, websocket: WebSocket, thread_id):

    dict_inputs = {"user_query": message}

    # Use new thread id to clear the chat history
    thread = {"configurable": {"thread_id": str(thread_id)}}

    async for event in workflow.astream(dict_inputs, thread, stream_mode="updates"):

        if "__interrupt__" in event:
            formatted = print_workflow(event)
            await websocket.send_text(formatted)
            await websocket.send_text("Type `ok` if looks good: ")
            feedback = await websocket.receive_text()
            if "ok" in feedback.lower():
                await workflow.ainvoke(
                    Command(resume={"action": "continue", "data": None}), config=thread
                )
            else:
                await workflow.ainvoke(
                    Command(resume={"action": "reject", "data": None}),
                    config=thread,
                )

    # Process image output
    state_hist = await workflow.aget_state(thread)
    if "image_output" in state_hist.values:
        image_name = state_hist.values["image_output"]
        if image_name:
            image_data = get_image_binary(image_name + ".png")
            await websocket.send_text(f"data:image/png;base64,{image_data}")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:  # Changed NoReturn to None
    await websocket.accept()
    thread_id = 1
    while True:
        client_msg = await websocket.receive_text()

        await chat(client_msg, websocket, thread_id)

        thread_id += 1


@app.get("/")
async def web_app() -> HTMLResponse:
    return HTMLResponse(html)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

# uvicorn webui.main:app --reload
