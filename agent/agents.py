from typing import TypedDict

from agent.ollama_models import OllamaModel
from agent.gpt_models import GPTModel
from agent.prompts import (
    generate_retriever_sys_prompt,
    generate_insitu_sys_prompt,
    generate_fluid_sub_sys_prompt,
)
from qi.qi_lang import parse_tool_call
from langgraph.types import Command, interrupt
from tools.tool_exec import execute_tools


# Define the state object for the agent graph
class AgentGraphState(TypedDict):
    user_query: str
    retriever_response: list
    insitu_response: list
    fluid_sub_response: list
    insitu_next: str
    tool_calls: list
    image_output: str


class Agent:
    def __init__(
        self,
        state: AgentGraphState,
        model=None,
        temperature=0,
        model_endpoint=None,
        stop=None,
        guided_json=None,
    ):
        self.state = state
        self.model = model
        self.temperature = temperature
        self.model_endpoint = model_endpoint
        self.stop = stop
        self.guided_json = guided_json

    def get_llm(self, model_name="gpt-4o"):
        if model_name == "gpt-4o":
            return GPTModel(model=self.model, temperature=self.temperature)
        else:
            return OllamaModel(model=self.model, temperature=self.temperature)

    def update_state(self, key, value):
        if isinstance(self.state.get(key), list):
            self.state[key].append(value)
        elif key == "insitu_next":
            # TODO: Really bad here. Just get it working
            self.state[key] = value
        else:
            self.state[key] = [value]

    def pack_message(self, system_message, user_message):
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": f"user query: {user_message}"},
        ]

        return messages


class RetrieverAgent(Agent):
    def invoke(self, user_query):

        retriever_prompt = generate_retriever_sys_prompt()
        messages = self.pack_message(retriever_prompt, user_query)

        llm = self.get_llm()
        ai_msg = llm.invoke(messages)
        response = ai_msg.content

        print(f"RetrieverAgent: {response}")

        self.update_state("retriever_response", response)
        self.update_state("tool_calls", parse_tool_call(response))
        return self.state


class InsituAgent(Agent):
    def invoke(self, user_query):

        insitu_prompt = generate_insitu_sys_prompt()
        messages = self.pack_message(insitu_prompt, user_query)

        llm = self.get_llm()
        ai_msg = llm.invoke(messages)
        response = ai_msg.content

        print(f"InsituAgent: {response}")

        self.update_state("insitu_response", response)

        r = parse_tool_call(response)

        if not r["tool_call"]:
            self.update_state("insitu_next", ["human_review"])

        elif r["tool_call"]["name"] != "perform_fluid_substitution":
            self.update_state("insitu_next", ["human_review"])
            self.update_state("tool_calls", r)
        else:
            self.update_state("insitu_next", ["fluid_sub"])
            self.update_state("tool_calls", r)

        return self.state


class FluidSubstituteAgent(Agent):
    def invoke(self, user_query):

        fluid_sub_prompt = generate_fluid_sub_sys_prompt()
        messages = self.pack_message(fluid_sub_prompt, user_query)

        llm = self.get_llm()
        ai_msg = llm.invoke(messages)
        response = ai_msg.content

        r = parse_tool_call(response)
        print(f"FluidSubstituteAgent: {response}")

        self.update_state("fluid_sub_response", response)
        self.update_state("tool_calls", r)

        return self.state


class HumanReviewAgent(Agent):
    def human_review_node(self):

        human_review = interrupt(
            {
                "workflow": self.state["tool_calls"],
            }
        )

        review_action = human_review["action"]
        review_data = human_review.get("data")

        if review_action == "continue":
            return "continue", None

        elif review_action == "reject":
            return "feedback", review_data

    def invoke(self):
        route, msg = self.human_review_node()
        if route == "continue":
            tool_list = self.state["tool_calls"]
            try:
                image_name = execute_tools(tool_list)
            except:
                print(f"Warning: Execution fails ... {tool_list}")
                image_name = None
        else:
            image_name = None

        return Command(goto="end", update={"image_output": image_name})
