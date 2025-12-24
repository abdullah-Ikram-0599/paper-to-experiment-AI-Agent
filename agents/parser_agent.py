from smolagents import ToolCallingAgent
from core.model import get_model
from agents.prompts.parser_prompt import SYSTEM_PROMPT


class ParserAgent:

    def __init__(self):

        self.agent =ToolCallingAgent(tools=[], model=get_model())
        
    def parse_paper(self,text):
    
        return self.agent.run(SYSTEM_PROMPT + "\n\n" + text[:12000])
