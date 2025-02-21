
from qi import *

def get_whole_log(well_name:str) -> QIWell:
    """
    Retrieve the entire well log for a specified well name.
        Args:
        well_name (str): well_name
    """
    return

def get_log_interval_by_unit(well_name: str, unit: str) -> QIWell:
    """
    Retrieve a part of a well log at a specific geological unit or formation.
    Args:
        well_name (str): well_name
        unit (str): The geological unit or formation name
    """
    return

def get_log_interval_by_depth(well_name: str, min_depth: float, max_depth: float, depth_col: str) -> QIWell:
    """
    Retrieve a part of a well log a specific depth interval.
    Args:
        well_name (str): well_name
        min_depth (float): The starting depth of the interval.
        max_depth (float): The ending depth of the interval.
        depth_col (str): The depth column used for filtering ("MD" or "TVDSS").
    """
    return

def plot_logs_from_well(well_name: str, log_list: list[str], depth_col:str):
    """
    Plot specified logs from a well log object.
    This function generates plots for selected logs (e.g., "RHOB", "PHIE", "Sw", "Facies" etc.) 
    from a provided well_name.
    Use this mapping from user query to log_list: list[str]
        Density: "RHOB",
        Porosity: "PHIE",
        Shale Volume or V shale: "Vsh",
        Water saturation: "Sw,"
        Sonic log: "DTC",
        Shear log: "DTS",
        Lithology log: "LITHO",
        Fluid log: "Fluid"
        Acoustic Impedance or AI: "AI"
        Vp/Vs: "Vp/Vs"

    for example, if user wants to plot porosity and sonic log, then the log_list is ["PHIE", "DTC"]
    Args:
        well_name (str): well name
        log_list (list[str]): A list of log names to include in the plot.
        depth_col (str): The depth column used for plotting ("MD" or "TVDSS").
    """
    return

def plot_crossplot_insitu_condition(well_name: str, x_attr:str, y_attr: str, facies_list: list[str]):
    """
    Generate a crossplot of in-situ conditions for specified attributes and facies.
    Use this mapping from user query of x_attr and y_attr to the follow string
        Density: "RHOB",
        Porosity: "PHIE",
        Shale Volume or V shale: "Vsh",
        Water saturation: "Sw,"
        Sonic log: "DTC",
        Shear log: "DTS",
        Lithology log: "LITHO",
        Fluid log: "Fluid"
        Acoustic Impedance or AI: "AI"
        Vp/Vs: "Vp/Vs"

    for example, if user wants to plot porosity in x_attr and Density in y_attr 
    then x_attr is 'PHIE' and y_attr is 'RHOB'

    Args:
        well_name (str): well name
        x_attr (str): The attribute for the x-axis (e.g., "AI").
        y_attr (str): The attribute for the y-axis (e.g., "Vp/Vs").
        facies_list (list[str]): list of facies
    """
    return

def plot_crossplot_fluid_sub_condition(well_name: str, x_attr:str, y_attr: str, facies_list: list[str]):
    """
    Generate a crossplot for attributes after fluid substitution.
    Use this mapping from user query of x_attr and y_attr to the follow string
        Density: "RHOB",
        Porosity: "PHIE",
        Shale Volume or V shale: "Vsh",
        Water saturation: "Sw,"
        Sonic log: "DTC",
        Shear log: "DTS",
        Lithology log: "LITHO",
        Fluid log: "Fluid"
        Acoustic Impedance or AI: "AI"
        Vp/Vs: "Vp/Vs"
        
    for example, if user wants to plot porosity in x_attr and Density in y_attr 
    then x_attr is 'PHIE' and y_attr is 'RHOB'
    
    Args:
        well_name (str): well name
        x_attr (str): The attribute for the x-axis (e.g., "AI").
        y_attr (str): The attribute for the y-axis (e.g., "Vp/Vs").
        facies_list (list[str]): list of facies

    Returns:
        None: The function displays the crossplot.
    """
    return

def perform_fluid_substitution(well_name: str, hc_type: str, hc_sat: float, vsh_cut: float, mod_Sw: bool) -> QIWell:
    """
    Perform fluid substitution

    Args:
        well_name (str): well name.
        hc_type (str): The hydrocarbon type for substitution ("oil", "gas", or "brine").
        hc_sat (float): The desired fluid saturation (range: 0.0 to 1.0).
        vsh_cut (float, optional): The maximum shale volume for clean sand (default: 0.2).
        mod_Sw (bool, optional): Whether to modify the original water saturation log (default: True).
    """
    return

def compute_facies_separability(well_name: str, log_name:str, facies_list: list[str]):
    """
    Compute the separability of specified property log between facies of the well
    Args:
        well_name (str): well name.
        log_name (str): The property for separation computation, usually is acoustic impedance (AI)
        facies_list (list[str]): A list of facies names to evaluate separability 
                                 (e.g., "shale", "brine", "gas").
    """
    return

def plot_depth_trend_insitu_condition(well_name: str, log_name: str, depth_col: str):
    """
    Plot the depth trend of a specified log attribute under in-situ conditions.
    Use this mapping from user query of log_name to the follow string
        Density: "RHOB",
        Porosity: "PHIE",
        Shale Volume or V shale: "Vsh",
        Water saturation: "Sw,"
        Sonic log: "DTC",
        Shear log: "DTS",
        Lithology log: "LITHO",
        Fluid log: "Fluid"
        Acoustic Impedance or AI: "AI"
        Vp/Vs: "Vp/Vs"

    for example, if user wants to plot porosity then log_name is 'PHIE'
    Args:
        well_name (str): well name.
        log_name (str): The name of the log attribute to plot (e.g., "AI").
        depth_col (str): The depth column used for the x-axis ("MD" or "TVDSS").
    """
    return

def plot_depth_trend_fluid_sub_condition(well_name: str, log_name: str, depth_col: str):
    """
    Plot the depth trend of a specified log attribute after fluid substitution.
    Use this mapping from user query of log_name to the follow string
        Density: "RHOB",
        Porosity: "PHIE",
        Shale Volume or V shale: "Vsh",
        Water saturation: "Sw,"
        Sonic log: "DTC",
        Shear log: "DTS",
        Lithology log: "LITHO",
        Fluid log: "Fluid"
        Acoustic Impedance or AI: "AI"
        Vp/Vs: "Vp/Vs"

    for example, if user wants to plot porosity then log_name is 'PHIE'
    Args:
        well_name (str): well name.
        log_name (str): The name of the log attribute to plot (e.g., "AI").
        depth_col (str): The depth column used for the x-axis ("MD" or "TVDSS").

    """
    return

def generate_upscale_well(well_name: str, window:float , stride: float):
    """
    Generate an upscaled version of well

    Args:
        well_name (str): well name.
        window (float): The size of the smoothing window in meters.
        stride (float): The distance in meters between the center points of smoothing windows.
    """
    return

from semantic_router.utils.function_call import FunctionSchema

# Convert to function definition for system prompt
get_whole_log_schema = FunctionSchema(get_whole_log).to_ollama()
get_log_interval_by_unit_schema = FunctionSchema(get_log_interval_by_unit).to_ollama()
get_log_interval_by_depth_schema =  FunctionSchema(get_log_interval_by_depth).to_ollama()
plot_logs_from_well_schema = FunctionSchema(plot_logs_from_well).to_ollama()

plot_crossplot_insitu_condition_schema = FunctionSchema(plot_crossplot_insitu_condition).to_ollama()
plot_crossplot_fluid_sub_condition_schema = FunctionSchema(plot_crossplot_fluid_sub_condition).to_ollama()
perform_fluid_substitution_schema =  FunctionSchema(perform_fluid_substitution).to_ollama()
compute_facies_separability_schema = FunctionSchema(compute_facies_separability).to_ollama()

plot_depth_trend_insitu_condition_schema =  FunctionSchema(plot_depth_trend_insitu_condition).to_ollama()
plot_depth_trend_fluid_sub_condition_schema = FunctionSchema(plot_depth_trend_fluid_sub_condition).to_ollama()

generate_upscale_well_schema = FunctionSchema(generate_upscale_well).to_ollama()

# Function Definitions
# Retriever Agent
get_whole_log_def = json.dumps(get_whole_log_schema, indent=2)
get_log_interval_by_unit_def =  json.dumps(get_log_interval_by_unit_schema, indent=2)
get_log_interval_by_depth_def =   json.dumps(get_log_interval_by_depth_schema, indent=2)
# Insitu Agent
plot_logs_from_well_def =  json.dumps(plot_logs_from_well_schema, indent=2)
plot_crossplot_insitu_condition_def = json.dumps(plot_crossplot_insitu_condition_schema, indent=2)
plot_depth_trend_insitu_condition_def =   json.dumps(plot_depth_trend_insitu_condition_schema, indent=2)
perform_fluid_substitution_def = json.dumps(perform_fluid_substitution_schema, indent=2)
# FluidSubstitute Agent
plot_crossplot_fluid_sub_condition_def =  json.dumps(plot_crossplot_fluid_sub_condition_schema, indent=2)
plot_depth_trend_fluid_sub_condition_def =  json.dumps(plot_depth_trend_fluid_sub_condition_schema, indent=2)
compute_facies_separability_def = json.dumps(compute_facies_separability_schema, indent=2)


generate_upscale_well_def = json.dumps(generate_upscale_well_schema, indent=2)

# Prompts for each agent
retriever_prompt_template = f"""<|start_header_id|>system<|end_header_id|>
You are a function calling AI model speciafically dealing with retriving the data. 
You are provided with function signatures within <tools></tools> XML tags. 
You may call one and only one functions to assist with the user query. 
Don't make assumptions about what values to plug into functions. 
If decided to call a function, return a json object with function name and arguments within <tool_call></tool_call> XML tags as follows:

<tool_call>{{"name": <function-name>,"arguments": <args-dict>}}</tool_call>

You have 3 tools to choose from. Here are the available tools:

 <tool_call>{get_whole_log_def}</tool_call>
 <tool_call>{get_log_interval_by_unit_def}</tool_call>
 <tool_call>{get_log_interval_by_depth_def}</tool_call>

 For example, user's query: can you go get the well BA-18 from 1763 to 2311 m MD. Do fluid substitution for gas with 0.9 saturation. After that, plot its AI depth trend log
 return object is <tool_call>{{"name": "get_log_interval_by_depth", "arguments": {{"well_name": "BA-18", "min_depth": 1763, "max_depth": 2311, "depth_col": "MD"}}}}</tool_call>

 Only return one tool call.

 <|eot_id|><|start_header_id|>user<|end_header_id|>
"""

def generate_insitu_sys_prompt(well_name: str):

    insitu_prompt_template =f"""<|start_header_id|>system<|end_header_id|>

    You are a function calling AI model specifically deal with insitu well. 
    You are given the well_name {well_name} from previous agent. 
    You are provided with function signatures within <tools></tools> XML tags.
    You may call one and only one function to assist with the user query. 
    Don't make assumptions about what values to plug into functions. 
     If decided to call a function, return a json object with function name and arguments 
    within <tool_call></tool_call> XML tags as follows:
    
    <tool_call>{{"name": "<function-name>", "arguments": <args-dict>}}</tool_call>

    You have 4 tools (3 for plotting and 1 for fluid substitution) to choose from. 
    Here are the available tools:
    """

    insitu_tools_def = f"""
    <tool_call>{plot_logs_from_well_def}</tool_call>
    <tool_call>{plot_crossplot_insitu_condition_def}</tool_call>
    <tool_call>{plot_depth_trend_insitu_condition_def}</tool_call>
    <tool_call>{perform_fluid_substitution_def}</tool_call>

    
    For example, user's query:get the unit 2A of well BA-18. Do fluid substitution for oil with 0.9 saturation. After that, plot the AI and Vp/Vs crossplot.
    return object is  <tool_call>{{"id": 0, "name": "perform_fluid_substitution", "arguments": {{"well_name": "{well_name}", "hc_type": "oil", "hc_sat": 0.9}}}}</tool_call>
    
    Only return one tool call.

    <|eot_id|><|start_header_id|>user<|end_header_id|>
    """

    return insitu_prompt_template + insitu_tools_def

def generate_fluid_sub_sys_prompt(well_name: str):
    
    fluid_sub_prompt_template = f"""<|start_header_id|>system<|end_header_id|>

    You are a function calling AI model specifically deal with fluid-substituted well. 
    You are given the well_name {well_name} from previous agent. 
    You are provided with function signatures within <tools></tools> XML tags.You may call one and only one function to assist with the user query. 
    Don't make assumptions about what values to plug into functions. 
    If decided to call a function, return aeturn a json object with function name and arguments 
    within <tool_call></tool_call> XML tags as follows:
    
    <tool_call>{{"name": "<function-name>", "arguments": <args-dict>}}</tool_call>

    You have 3 tools (2 for plotting and 1 for compute separation) to choose from. 
    Here are the available tools:
    """

    fluid_sub_tools_def = f"""
    <tool_call>{plot_crossplot_fluid_sub_condition_def}</tool_call>
    <tool_call>{plot_depth_trend_fluid_sub_condition_def}</tool_call>
    <tool_call>{compute_facies_separability_def}</tool_call>

    For example, user's query: can you go get the well BA-18 from 1763 to 2311 m MD. Do fluid substitution for gas with 0.9 saturation. After that, plot its AI depth trend log
    return object is <tool_call>{{"id": 0, "name": "plot_depth_trend_fluid_sub_condition", "arguments": {{"well_name": "{well_name}", "log_name": "AI", "depth_col": "MD"}}}}</tool_call>
    
    <|eot_id|><|start_header_id|>user<|end_header_id|>
    """

    return fluid_sub_prompt_template + fluid_sub_tools_def