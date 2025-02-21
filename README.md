# Quantitative Interpretation with LLM Chat Interface

## Features

### Quantitative Interpretation Logic

- **Data Visualization**
- **Fluid substitution**
- **Quantify Hydrocarbon Separation**

### LLM Chat Interface via Tool Calling

- **Groq** tool use

### Web UI

- **TBC**

## Repository Structure

```plaintext
├── agent/                          #
│   ├── agents.py                   #
│   ├── graphy.py                   #
│   ├── ollama_models.py            #
│   ├── prompts.py                  #
│   ├── state.py                    #
├── app/                            #
│   ├──app.py                       #
├── qi/                             #
│   ├──qi_dataloader.py             # (Only example)
│   ├──qi_lang.py                   # (TO CHANGE)
│   ├──qi_tools.py                  #
│   ├──qi_well.py                   #
├── tools/                          #
│   ├──fluid_substitute_tools.py    #
│   ├──retrieve_tools.py            #
│   ├──visualize_fluid_sub_tools.py #
│   ├──visualize_insitu_tools.py    #
├── data/                           #
│   ├── *.las                       #
├── data_server.py                  # (TO CHANGE)
└── README.md                       # Project documentation (this file)
```

### Test Coverage

- **TBC**
