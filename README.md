# Paper-to-Experiment AI Agent

A fully local, multi-agent AI system that converts a research paper (PDF) into a **structured experiment plan**.

The pipeline automates: 

**Paper → Parsing → Method Extraction → Experiment Design**

## Why This Project?

Research papers explain *what was done*, not *how to reproduce it*.  

This project bridges that gap by translating paper text into actionable experimental insights.   

- Runs **100% locally**
- No cloud APIs
- Focused on research understanding and experiment ideation

## Pipeline

PDF  
↓  
Text Extraction  
↓  
Parser Agent  
↓  
Method Agent  
↓  
Experiment Agent  

Each agent has a single responsibility, keeping the system modular and extensible.

## Project Structure

```
paper-to-experiment/
├── agents/
│   └── prompts/
├── utils/
├── outputs/
│   ├── text/
│   ├── parsed/
│   ├── method/
│   └── experiment/
└── main.py
```

## Usage:

**Step 1: Clone this repository:** 

```
git clone https://github.com/abdullah-Ikram-0599/paper-to-experiment-AI-Agent/
```

**Step 2: Install Required libraries:**

```
pip install -r requirements.txt
```

**Step 3: Pull the model from Ollama:** (Note: This requires 4.2 GB free space on local storage)

```
ollama pull krith/qwen2.5-coder-32b-instruct:IQ3_M
```

**Step 4: Place your research paper in the project root:**

```
paper-to-experiment/
└── paper.pdf
```

**Step 5: Run the pipeline:**

```
python main.py -- "paper.pdf"
```

**Step 6: Outputs are saved step-by-step inside the `outputs/` directory.**

```
outputs/
├── text/
│   └── attention_text.txt        # Raw extracted text
├── parsed/
│   └── attention_parsed.txt      # parsed paper
├── method/
│   └── attention_method.txt      # methodology
└── experiment/
    └── attention_experiment.txt  # Experiments
```

## Tech Stack

- Python
- Smolagents (from Hugging Face)
- Local LLMs via Ollama  
- Qwen-2.5-Instruct LLM.   
- Modular agent-based design  

## Intended Use

- ML / AI researchers  
- Graduate students  
- Research engineers  
- Translating papers into experiments  

## Limitations

- Does not execute experiments  
- Assumes standard ML paper structure  
- Output quality depends on LLM reasoning 
