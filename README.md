# Building LLM Agents for Seismic Quantitative Interpretation

[Public version | Prototype Phase = Ok]

## Features

### Seismic Quantitative Interpretation Logic

- **Data Visualization**
- **Fluid substitution**
- **Quantify Hydrocarbon Separation**

### LLM Chat Interface via Tool Calling

- Used Ollama with Llaam3-Groa-ToolUse:8b for tool calling

### Web UI

- Currently tested on localhost with single GPU

## Repository Structure

```plaintext
├── agent/                          #
│   ├── agents.py                   # LLM Agents
│   ├── graphy.py                   # workflow graph
│   ├── ollama_models.py            # llama endpoint
│   ├── prompts.py                  # function definition and system prompts
│   ├── state.py                    # shared state for agents
├── qi/                             #
│   ├──qi_dataloader.py             # Example. Modify according to yours
│   ├──qi_lang.py                   # Parser
│   ├──qi_tools.py                  # QI Logic
│   ├──qi_well.py                   # Well object
├── tools/                          # wrappers for legacy functions for LLM
│   ├──fluid_substitute_tools.py    #
│   ├──retrieve_tools.py            #
├──visualize_fluid_sub_tools.py     # 
│   ├──visualize_insitu_tools.py    #
├── webui/                          #
│   ├──index.html                   # page for chat interface
│   ├──main.py                      # serving local host
|   ├──data_server.py               # Pre-load well data to memory, serve via HTTP
└── README.md                       # Project documentation (this file)
```

### Test Coverage

- **TBC**
- Planned to log user prompts (any) and write test for expected tool calling sequence
