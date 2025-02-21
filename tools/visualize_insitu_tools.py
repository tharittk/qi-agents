from agent.state import AgentGraphState
from qi.qi_tools import plot_logs, plot_crossplot_insitu, plot_depth_trend_insitu
from qi.qi_lang import parse_tool_call


def plot_logs_wrap(state, well_name, log_list, depth_col):
    well = state["database"][well_name]

    img_name = plot_logs(well, log_list, depth_col, save_fig=True)
    
    state["image_output"] = "<output_image>"+img_name+"</output_image>"

    print("Execute plot logs..")

    return

def plot_crossplot_insitu_wrap(state, well_name, x_attr, y_attr, facies_list):
    well = state["database"][well_name]

    print("Execute crossplot insitu..")
    img_name = plot_crossplot_insitu(well, x_attr, y_attr, facies_list, save_fig=True)

    state["image_output"] = "<output_image>"+img_name+"</output_image>"

    return

def plot_depth_trend_insitu_wrap(state, well_name, log_name, depth_col):
    well = state["database"][well_name]
    
    print("Execute depth trend insitu..")
    img_name = plot_depth_trend_insitu(well, log_name, depth_col, save_fig=True)

    state["image_output"] = "<output_image>"+img_name+"</output_image>"

    return

visualize_insitu_function_table = {
    "plot_logs_from_well": plot_logs_wrap,
    "plot_crossplot_insitu_condition": plot_crossplot_insitu_wrap,
    "plot_depth_trend_insitu_condition": plot_depth_trend_insitu_wrap,
}


# visualization should not return anything
def visualize_insitu(state: AgentGraphState, query=None):
    query_value = query() if callable(query) else query

    query = parse_tool_call(query_value.content)

    if query['tool_call']:
        function_name = query['tool_call']['name']
        function_args = query['tool_call']['arguments']

        function_args["state"] = state

        f = visualize_insitu_function_table[function_name]
        
        f(**function_args)

        return state
    else:
        # back to end by default

        return state
