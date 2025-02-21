from agent.state import AgentGraphState
from agent.ollama_models import OllamaModel
from agent.prompts import (
    retriever_prompt_template,
    generate_insitu_sys_prompt,
    generate_fluid_sub_sys_prompt
)
from qi.qi_lang import parse_tool_call

class Agent:
    def __init__(self, state: AgentGraphState, model=None, server=None,
                 temperature=0, model_endpoint=None, stop=None, guided_json=None):
        self.state = state
        self.model = model
        self.server = server
        self.temperature = temperature
        self.model_endpoint = model_endpoint
        self.stop = stop
        self.guided_json = guided_json
    
    def get_llm(self, json_model=False):
        assert self.server == 'ollama'
        #OllamaJSONModel(model=self.model, temperature=self.temperature) if json_model else
        return OllamaModel(model=self.model, temperature=self.temperature)
    
    def update_state(self, key, value):
        self.state = {**self.state, key: value}

class RetrieverAgent(Agent):
    def invoke(self, user_query, prompt=retriever_prompt_template):

        # no parameter in prompt template
        retriever_prompt = prompt

        messages = [
            {"role": "system", "content": retriever_prompt},
            {"role": "user", "content": f"user query: {user_query}"}
        ]

        llm = self.get_llm()
        ai_msg = llm.invoke(messages)
        response = ai_msg.content

        print(f"RetrieverAgent: {response}")

        self.update_state("retriever_response", response)
        return self.state
    
class InsituAgent(Agent):
    def invoke(self, user_query, retrieved_data=None):
        retrieved_data = retrieved_data() if callable(retrieved_data) else retrieved_data
        target_well = str(retrieved_data.content)
        insitu_prompt = generate_insitu_sys_prompt(target_well)

        messages = [
            {"role": "system", "content": insitu_prompt},
            {"role": "user", "content": f"user query: {user_query}"}
        ]

        llm = self.get_llm()
        ai_msg = llm.invoke(messages)
        response = ai_msg.content

        print(f"InsituAgent: {response}")

        self.update_state("insitu_response", response)

        r = parse_tool_call(response)


        # for conditional edges
        if not r["tool_call"]:
            self.update_state("conditional_response", ["end"])
        elif r['tool_call']['name'] == "perform_fluid_substitution":
            # update conditional based on response
            self.update_state("conditional_response", ["fluid_sub_tool"] )
        else:
            self.update_state("conditional_response", ["vis_insitu_tool"])
        
        return self.state

class FluidSubstituteAgent(Agent):
    def invoke(self, user_query, fluid_sub_well=None):
        fluid_sub_well = fluid_sub_well() if callable(fluid_sub_well) else fluid_sub_well
        
        target_well = str(fluid_sub_well.content)
        fluid_sub_prompt = generate_fluid_sub_sys_prompt(target_well)

        messages = [
            {"role": "system", "content": fluid_sub_prompt},
            {"role": "user", "content": f"user query: {user_query}"}
        ]

        llm = self.get_llm()
        ai_msg = llm.invoke(messages)
        response = ai_msg.content

        print(f"FluidSubstituteAgent: {response}")

        self.update_state("fluid_sub_response", response)

        return self.state

class EndNodeAgent(Agent):
    def invoke(self):
        self.update_state("end_chain", "end_chain")
        return self.state

def check_for_content(var):
    if var:
        try:
            var = var.content
            return var.content
        except:
            return var
    else:
        var
