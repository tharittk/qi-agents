from langgraph.graph import StateGraph, END

from agent.agents import (
    RetrieverAgent,
    InsituAgent,
    FluidSubstituteAgent,
    EndNodeAgent
)
from agent.state import AgentGraphState, get_agent_graph_state
from agent.prompts import(
    retriever_prompt_template,
)
from tools.retrieve_tools import retrieve_well_from_database
from tools.visualize_insitu_tools import visualize_insitu
from tools.fluid_substitute_tools import fluid_substitute
from tools.visualize_fluid_sub_tools import visualize_fluid_sub

from qi.qi_dataloader import load_exp_wells

def create_graph(server=None, model=None, stop=None, model_endpoint=None, temperature=0):
    graph = StateGraph(AgentGraphState)

    def load_database(state: AgentGraphState):
        return {"database": {}}
    
    graph.add_node("init_db", load_database)

    graph.add_node(
        "retriever",
        lambda state: RetrieverAgent(
            state=state,
            model=model,
            server=server,
            stop=stop,
            model_endpoint=model_endpoint,
            temperature=temperature
        ).invoke(
            user_query=state["user_query"],
            prompt=retriever_prompt_template
        )
    )

    graph.add_node(
        "retrieve_tool",
        lambda state: retrieve_well_from_database(
            state=state,
            query=lambda: get_agent_graph_state(state=state, state_key="retriever_latest")
        )
    )

    graph.add_node(
        "insitu",
        lambda state: InsituAgent(
            state=state,
            model=model,
            server=server,
            stop=stop,
            model_endpoint=model_endpoint,
            temperature=temperature
        ).invoke(
            user_query=state["user_query"],
            retrieved_data=lambda: get_agent_graph_state(state=state, state_key="retrieve_tool_latest"),        
        )
    )

    # two branches
    graph.add_node(
        "vis_insitu_tool",
        lambda state: visualize_insitu(
            state=state,
            query=lambda: get_agent_graph_state(state=state, state_key="insitu_latest")
        )
    )

    graph.add_node(
        "fluid_sub_tool",
        lambda state: fluid_substitute(
            state=state,
            query=lambda: get_agent_graph_state(state=state, state_key="insitu_latest")

        )
    )

    graph.add_node(
        "fluid_sub",
        lambda state: FluidSubstituteAgent(
            state=state,
            model=model,
            server=server,
            stop=stop,
            model_endpoint=model_endpoint,
            temperature=temperature
        ).invoke(
            user_query=state["user_query"],
            fluid_sub_well=lambda: get_agent_graph_state(state=state, state_key="fluid_sub_tool_latest")
        )
    )

    graph.add_node(
        "vis_fluid_sub_tool",
        lambda state: visualize_fluid_sub(
            state=state,
            query=lambda: get_agent_graph_state(state=state, state_key="fluid_sub_latest")
        )
    )

    graph.add_node("end", lambda state: EndNodeAgent(state).invoke())

    # Connect the node
    graph.set_entry_point("init_db")
    graph.set_finish_point("end")
    graph.add_edge("init_db", "retriever")
    graph.add_edge("retriever", "retrieve_tool")
    #graph.add_edge("retrieve_tool", "insitu")

    def should_continue(state, next_if_yes=""):
        feedback = str(get_agent_graph_state(state=state, state_key="retrieve_tool_latest").content) 
        if feedback == "end":
            return "end"
        return next_if_yes
    
    # bad prompt, not incur tool calling
    graph.add_conditional_edges(
        "retrieve_tool",
        lambda state: (
            should_continue(state, "insitu")
        )
    )

    graph.add_conditional_edges(
        "insitu",
        lambda state: get_agent_graph_state(state=state, state_key="conditional_latest")
    )

    graph.add_edge("vis_insitu_tool", "end")
    #graph.add_edge("fluid_sub_tool", "fluid_sub")

    # bad prompt, not incur tool calling
    graph.add_conditional_edges(
        "fluid_sub_tool",
        lambda state: (
            should_continue(state, "fluid_sub")
        )
    )

    graph.add_edge("fluid_sub", "vis_fluid_sub_tool")
    graph.add_edge("vis_fluid_sub_tool", "end")

    return graph

def compile_workflow(graph):
    workflow = graph.compile()
    return workflow