import re
import json


def parse_tool_call(input_string):
    pattern = r"<tool_call>(.*?)</tool_call>"
    match = re.search(pattern, input_string)

    if match:
        try:
            json_data = match.group(1).strip()
            tool_call_data = json.loads(json_data)

            result = {
                "tool_call": {
                    "name": tool_call_data.get("name"),
                    "arguments": tool_call_data.get("arguments"),
                }
            }
            # print("Sucessfully parse:: ", result)
        except json.JSONDecodeError:
            result = {"tool_call": None}
    else:
        result = {"tool_call": None}

    return result


if __name__ == "__main__":

    two_calls = """<tool_call>{"id": 0, "name": "plot_depth_trend_fluid_sub_condition", "arguments": {"well_name": "BA-18_ext_sub", "log_name": "AI", "depth_col": "TVDSS"}}</tool_call>
    <tool_call>{"id": 1, "name": "compute_facies_separability", "arguments": {"well_name": "BA-18_ext_sub", "log_name": "AI", "facies_list": ["shale", "brine", "gas"]}}</tool_call>
    """

    one_call = """<tool_call>{"id": 0, "name": "plot_depth_trend_fluid_sub_condition", "arguments": {"well_name": "BA-18_ext_sub", "log_name": "AI", "depth_col": "TVDSS"}}</tool_call>
    """

    print(parse_tool_call(two_calls))
    print(parse_tool_call(one_call))
