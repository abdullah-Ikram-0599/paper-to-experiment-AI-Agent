from smolagents import ToolCallingAgent
from core.model import get_model
from agents.prompts.method_prompt import SYSTEM_PROMPT



class MethodAgent:

    def __init__(self):

        self.agent = ToolCallingAgent(tools=[], model=get_model())
        
    def extract_method(self,parsed_text):
    
        return self.agent.run(SYSTEM_PROMPT + "\n\n" + parsed_text)
