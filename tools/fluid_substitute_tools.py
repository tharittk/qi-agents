from agent.state import AgentGraphState
from qi.qi_tools import substitute_fluid
from qi.qi_lang import parse_tool_call

def substitute_fluid_wrap(state, well_name, hc_type, hc_sat, vsh_cut=0.2, mod_Sw=True):
    well = state["database"][well_name]

    print("execute fluid substitution...")

    # Substitute with brine is always implicit as all HCs are compared with brine
    sub_well = substitute_fluid(well, "brine", 1.0, vsh_cut, mod_Sw)

    sub_well = substitute_fluid(sub_well, hc_type, hc_sat, vsh_cut, mod_Sw)
    sub_name = well_name + "_sub"

    state["database"][sub_name] = sub_well

    return sub_name

def fluid_substitute(state: AgentGraphState, query=None):
    query_value = query() if callable(query) else query

    query = parse_tool_call(query_value.content)

    if query['tool_call']:
        function_name = query['tool_call']['name']
        function_args = query['tool_call']['arguments']
        
        # append
        function_args["state"] = state

        f = substitute_fluid_wrap

        well_sub = f(**function_args)

        state = {**state, "fluid_sub_tool_response": f"{well_sub}"}

        return state
    else:
        state = {**state, "fluid_sub_tool_response": "end"}

        return state