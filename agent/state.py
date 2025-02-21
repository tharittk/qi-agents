from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages

# Define the state object for the agent graph
class AgentGraphState(TypedDict):
    database: dict
    user_query: str
    retriever_response: Annotated[list, add_messages]
    retrieve_tool_response: Annotated[list, add_messages]
    insitu_response: Annotated[list, add_messages]
    fluid_sub_tool_response: Annotated[list, add_messages]
    fluid_sub_response: Annotated[list, add_messages]
    end_chain: Annotated[list, add_messages]

    condational_response: Annotated[list, add_messages]

    image_output: Annotated[list, add_messages]


# Define the nodes in the agent graph
def get_agent_graph_state(state: AgentGraphState, state_key: str):
    match state_key:
        case "database":
            return state["database"]
        
        case "retriever_latest":
            if state["retriever_response"]:
                return state["retriever_response"][-1]
            else:
                return state["retriever_response"]
            
        case "retrieve_tool_latest":
            if state["retrieve_tool_response"]:
                return state["retrieve_tool_response"][-1]
            else:
                return state["retrieve_tool_response"]

        case "insitu_latest":
            if state["insitu_response"]:
                return state["insitu_response"][-1]
            else:
                return state["insitu_response"]

        case "conditional_latest":
            if state["conditional_response"]:
                return state["conditional_response"][-1]
            else:
                return state["conditional_response"]

        case "fluid_sub_tool_latest":
            if state["fluid_sub_tool_response"]:
                return state["fluid_sub_tool_response"][-1]
            else:
                return state["fluid_sub_tool_response"]

        case "fluid_sub_latest":
            if state["fluid_sub_response"]:
                return state["fluid_sub_response"][-1]
            else:
                return state["fluid_sub_response"]
        
        case _:
            return None

