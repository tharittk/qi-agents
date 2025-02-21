import socket
import pickle
import struct

from agent.state import AgentGraphState, get_agent_graph_state
from qi.qi_tools import extract_log_interval_by_unit, extract_log_interval_by_depth
from qi.qi_lang import parse_tool_call

def extract_log_interval_by_unit_wrap(state:AgentGraphState, well_name, unit):
    well = query_server(well_name)

    extracted = extract_log_interval_by_unit(well, unit)
    extracted_name = well_name + "_ext"

    state["database"][extracted_name] = extracted

    return extracted_name

def extract_log_interval_by_depth_wrap(state: AgentGraphState, well_name, min_depth, max_depth, depth_col):
    well = query_server(well_name)
    
    extracted = extract_log_interval_by_depth(well, min_depth, max_depth, depth_col)
    extracted_name = well_name + "_ext"

    state["database"][extracted_name] = extracted

    return extracted_name

def extract_whole_log_wrap(state: AgentGraphState, well_name):
    extracted = query_server(well_name)
    
    state["database"][well_name] = extracted

    return well_name

retrieve_function_table = {
    "get_log_interval_by_unit": extract_log_interval_by_unit_wrap,
    "get_log_interval_by_depth": extract_log_interval_by_depth_wrap,
    "get_whole_log": extract_whole_log_wrap
}

def retrieve_well_from_database(state: AgentGraphState, query=None):
    query_value = query() if callable(query) else query

    #print("Query value content from retriever_latest: ", query_value.content)
    query = parse_tool_call(query_value.content)
    #print("After parsing: ", query)

    # extract function calling name and function argument
    if query['tool_call']:
        function_name = query['tool_call']['name']
        function_args = query['tool_call']['arguments']
        
        # append
        function_args["state"] = state

        f = retrieve_function_table[function_name]
        
        well_ext = f(**function_args)

        state = {**state, "retrieve_tool_response": f"{well_ext}"}

        return state
    else:
        state = {**state, "retrieve_tool_response": "end"}

        #print("Get state after update None:",get_agent_graph_state(state=state, state_key="retrieve_tool_latest"))
        return state

def query_server(key, host='localhost', port=9988):
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