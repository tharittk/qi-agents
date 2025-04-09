from qi.qi_tools import (
    # Retrieve
    extract_log_interval_by_unit,
    extract_log_interval_by_depth,
    # Insitu
    plot_logs,
    plot_crossplot_insitu,
    plot_depth_trend_insitu,
    # Fluid sub
    substitute_fluid,
    plot_crossplot_fluid_sub,
    compute_facies_separation_fluid_sub,
    plot_depth_trend_fluid_sub,
)


def extract_log_interval_by_unit_wrap(well_name, unit):
    well = query_server(well_name)
    extracted = extract_log_interval_by_unit(well, unit)
    return extracted


def extract_log_interval_by_depth_wrap(well_name, min_depth, max_depth, depth_col):
    well = query_server(well_name)
    extracted = extract_log_interval_by_depth(well, min_depth, max_depth, depth_col)
    return extracted


def extract_whole_log_wrap(well_name):
    extracted = query_server(well_name)
    return extracted


def plot_logs_wrap(well, log_list, depth_col):
    img_name = plot_logs(well, log_list, depth_col, save_fig=True)
    # state["image_output"] = "<output_image>" + img_name + "</output_image>"
    print("Execute plot logs..")
    return img_name


def plot_crossplot_insitu_wrap(well, x_attr, y_attr, facies_list):
    img_name = plot_crossplot_insitu(well, x_attr, y_attr, facies_list, save_fig=True)
    print("Execute crossplot insitu..")
    return img_name


def plot_depth_trend_insitu_wrap(well, log_name, depth_col):
    img_name = plot_depth_trend_insitu(well, log_name, depth_col, save_fig=True)
    print("Execute depth trend insitu..")
    return img_name


def plot_crossplot_fluid_sub_wrap(
    well, x_attr: str, y_attr: str, facies_list: list[str]
):
    img_name = plot_crossplot_fluid_sub(
        well, x_attr, y_attr, facies_list, save_fig=True
    )
    print("Execute Xplot after fluid substitution...")
    return img_name


def plot_depth_trend_fluid_sub_wrap(well, log_name, depth_col="TVDSS"):
    img_name = plot_depth_trend_fluid_sub(well, log_name, depth_col, save_fig=True)
    print("Execute depth trend fluid sub..")
    return img_name


def compute_facies_separation_fluid_sub_wrap(well, log_name, facies_list):
    img_name = compute_facies_separation_fluid_sub(
        well, log_name, facies_list, save_fig=True
    )
    print("Execute compute facies separation..")
    return img_name


def substitute_fluid_wrap(well, hc_type, hc_sat, vsh_cut=0.2, mod_Sw=True):
    # Substitute with brine is always implicit as all HCs are compared with brine
    sub_well = substitute_fluid(well, "brine", 1.0, vsh_cut, mod_Sw)
    sub_well = substitute_fluid(sub_well, hc_type, hc_sat, vsh_cut, mod_Sw)
    print("Execute fluid substitution...")
    return sub_well


function_table = {
    "get_log_interval_by_unit": extract_log_interval_by_unit_wrap,
    "get_log_interval_by_depth": extract_log_interval_by_depth_wrap,
    "get_whole_log": extract_whole_log_wrap,
    "plot_logs_from_well": plot_logs_wrap,
    "plot_crossplot_insitu_condition": plot_crossplot_insitu_wrap,
    "plot_depth_trend_insitu_condition": plot_depth_trend_insitu_wrap,
    "plot_crossplot_fluid_sub_condition": plot_crossplot_fluid_sub_wrap,
    "plot_depth_trend_fluid_sub_condition": plot_depth_trend_fluid_sub_wrap,
    "compute_facies_separability": compute_facies_separation_fluid_sub_wrap,
    "perform_fluid_substitution": substitute_fluid_wrap,
}

import socket, pickle, struct


def execute_tools(tool_list):
    tmp = None
    for tool in tool_list:
        function_name = tool["tool_call"]["name"]
        function_args = tool["tool_call"]["arguments"]

        f = function_table[function_name]

        if tmp:
            tmp = f(tmp, **function_args)
        else:
            tmp = f(**function_args)

    return tmp


def query_server(key, host="localhost", port=9988):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        client_socket.sendall(pickle.dumps(key))

        size_data = client_socket.recv(4)

        if not size_data:
            raise ValueError("Failed to receive data size header")

        data_size = struct.unpack("!I", size_data)[0]

        data = b""
        while len(data) < data_size:
            packet = client_socket.recv(4096)
            if not packet:
                break
            data += packet

        response = pickle.loads(data)
        print(f"Database response: {response}")

        client_socket.close()
        return response
    except Exception as e:
        print(f"Error querying server: {e}")
        client_socket.close()
        return None
