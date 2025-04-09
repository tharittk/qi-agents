from langgraph.graph import StateGraph, START

from agent.agents import (
    RetrieverAgent,
    InsituAgent,
    FluidSubstituteAgent,
    HumanReviewAgent,
)
from agent.agents import AgentGraphState


def create_graph(model=None, stop=None, model_endpoint=None, temperature=0):
    graph = StateGraph(AgentGraphState)
    common_params = {
        "model": model,
        "stop": stop,
        "model_endpoint": model_endpoint,
        "temperature": temperature,
    }
    graph.add_node(
        "retriever",
        lambda state: RetrieverAgent(state=state, **common_params).invoke(
            user_query=state["user_query"]
        ),
    )

    graph.add_node(
        "insitu",
        lambda state: InsituAgent(state=state, **common_params).invoke(
            user_query=state["user_query"],
        ),
    )

    graph.add_node(
        "fluid_sub",
        lambda state: FluidSubstituteAgent(state=state, **common_params).invoke(
            user_query=state["user_query"],
        ),
    )

    graph.add_node(
        "human_review",
        lambda state: HumanReviewAgent(state=state, **common_params).invoke(),
    )

    graph.add_node("end", lambda state: print("=== END OF SESSION ==="))

    # Connect the node
    graph.add_edge(START, "retriever")
    graph.add_edge("retriever", "insitu")
    graph.add_conditional_edges("insitu", lambda state: state["insitu_next"])
    graph.add_edge("fluid_sub", "human_review")

    return graph
