from agent.state import AgentGraphState
from qi.qi_tools import plot_crossplot_fluid_sub, compute_facies_separation_fluid_sub, plot_depth_trend_fluid_sub
from qi.qi_lang import parse_tool_call


def plot_crossplot_fluid_sub_wrap(state, well_name,  x_attr: str, y_attr: str, facies_list: list[str]):
    well = state["database"][well_name]

    print("Execute Xplot after fluid substitution...")

    img_name = plot_crossplot_fluid_sub(well, x_attr, y_attr, facies_list, save_fig=True)
    
    state["image_output"] = "<output_image>"+img_name+"</output_image>"

    return

def plot_depth_trend_fluid_sub_wrap(state, well_name, log_name, depth_col="TVDSS"):
    well = state["database"][well_name]

    print("Execute depth trend fluid sub..")

    img_name = plot_depth_trend_fluid_sub(well, log_name, depth_col, save_fig=True)

    state["image_output"] = "<output_image>"+img_name+"</output_image>"

    return

def compute_facies_separation_fluid_sub_wrap(state, well_name, log_name, facies_list):
    well = state["database"][well_name]

    print("Execute compute facies separation..")

    # TODO: compute multi substitution needs different chain invocation
    # has to assert the the facies exists..?

    img_name = compute_facies_separation_fluid_sub(well, log_name, facies_list, save_fig=True)
    
    state["image_output"] = "<output_image>"+img_name+"</output_image>"

    return

visualize_fluid_sub_function_table = {
    "plot_crossplot_fluid_sub_condition": plot_crossplot_fluid_sub_wrap,
    "plot_depth_trend_fluid_sub_condition":plot_depth_trend_fluid_sub_wrap,
    "compute_facies_separability": compute_facies_separation_fluid_sub_wrap,
}

def visualize_fluid_sub(state: AgentGraphState, query=None):
    query_value = query() if callable(query) else query

    query = parse_tool_call(query_value.content)

    if query['tool_call']:
        function_name = query['tool_call']['name']
        function_args = query['tool_call']['arguments']

        function_args["state"] = state

        f = visualize_fluid_sub_function_table[function_name]
        
        f(**function_args)

        return state
    else:

        # Back to end by default
        return state