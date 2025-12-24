# Paper-to-Experiment AI Agent

A fully local, multi-agent AI system that converts a research paper (PDF) into a **structured experiment plan**.

The pipeline automates: 

**Paper → Parsing → Method Extraction → Experiment Design**

--

## Why This Project?

Research papers explain *what was done*, not *how to reproduce it*.  
This project bridges that gap by translating paper text into actionable experimental setups.

- Runs **100% locally**
- No cloud APIs
- Focused on research understanding and experiment ideation

---

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

---

## Project Structure

paper-to-experiment/  
├── agents/  
    ├── prompts/
├── utils/  
├── outputs/  
│   ├── text/  
│   ├── parsed/  
│   ├── method/  
│   └── experiment/  
└── main.py  

---

## Usage

python main.py -- "paper_pdf_name"  

Outputs are saved step-by-step inside the `outputs/` directory.

---

## Tech Stack

- Python  
- Local LLMs via Ollama  
- Qwen-2.5-Instruct  
- Modular agent-based design  

---

## Intended Use

- ML / AI researchers  
- Graduate students  
- Research engineers  
- Translating papers into experiments  

---

## Limitations

- Does not execute experiments  
- Assumes standard ML paper structure  
- Output quality depends on LLM reasoning 
