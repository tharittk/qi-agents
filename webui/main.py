import asyncio
from typing import AsyncGenerator, NoReturn

import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from ollama import AsyncClient

from agent.graph import create_graph, compile_workflow
from langchain_core.messages.human import HumanMessage
from langchain_core.messages import AIMessage

import warnings
warnings.filterwarnings('ignore')

from base64 import b64encode
import re

# Agent graph
server = 'ollama'
model = 'llama3-groq-8b:Q8'
model_endpoint = None
iterations = 10
graph = create_graph(server=server, model=model, model_endpoint=model_endpoint)
workflow = compile_workflow(graph)


app = FastAPI()
with open("./webui/index.html") as f:
    html = f.read()



# async def chat(message):
#     messages = [{'role': 'user', 'content': f"{message}"}]
    
#     response = await AsyncClient().chat(
#         model='llama3.1:8b',
#         messages=messages, 
#         stream=True,
#         keep_alive="1m")
    
#     all_content = ""
#     async for chunk in response:
#         content = chunk['message']['content']
#         if content:
#             all_content += content
#             yield all_content

def get_image_binary(file_path):

    with open(file_path, "rb") as image_file:
        image_data = b64encode(image_file.read()).decode('utf-8')
        return image_data

# With agent

tool_pattern = r"<tool_call>\s*(.*?)\s*</tool_call>"
img_pattern = r"<output_image>\s*(.*?)\s*</output_image>"

# chat_interface_sys_prompt = '''
# The user will give you the JSON of the functional call. 
# As if you are executing the function, you have to phrase that what you are doing, 
# and what parameter you are using. Keep it short.
# "
# '''

async def chat(message, outputs):

    dict_inputs = {"user_query": message}
    limit = {"recursion_limit": iterations}

    streaming_content = ""

    async for event in workflow.astream(dict_inputs, limit, stream_mode="messages"):
        #TODO: Langgraph is weird. The AI message is label with HumanMessage
        # Probably due to type enforcement / annotation

        msg = event[0]
        if isinstance(msg, HumanMessage):
            content = msg.content

            if re.search(tool_pattern, content):
                pass

            elif re.search(img_pattern, content):
                match = re.search(img_pattern, content)
                # TODO: Any cleaner way than .png here.
                outputs.append(match.group(1) + '.png')
                pass

            else:
                continue
            
            content = content + "\n"

            streaming_content += content
            yield streaming_content
        streaming_content += "\n"


# TODO: Log file for historical user's query
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> NoReturn:
    await websocket.accept()
    while True:
        client_msg = await websocket.receive_text()
        log = open("./webui/user_log.txt", "a")
        log.write(client_msg + '\n')
        log.close()
        outputs = []
        async for text in chat(client_msg, outputs):
            #print("Text send: ", text)
            await websocket.send_text(text)

        if outputs:
            image_data = get_image_binary(outputs[0])
            await websocket.send_text(f"data:image/png;base64,{image_data}")

@app.get("/")
async def web_app() -> HTMLResponse:
    return HTMLResponse(html)


def main():
    asyncio.run(chat())

# Port fowarding : $ ssh -L 8000:localhost:8000 tharitt@corp-l-ws73
if __name__ == "__main__":
    uvicorn.run(
        "webui.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )