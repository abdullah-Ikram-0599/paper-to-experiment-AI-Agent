from smolagents import ToolCallingAgent
from core.model import get_model
from agents.prompts.experiment_prompt import SYSTEM_PROMPT


class ExperimentAgent:
    def __init__(self):
        self.agent = ToolCallingAgent(
            tools=[],
            model=get_model(),
           
        )

    def design_experiment(self, method_text):
        prompt = SYSTEM_PROMPT + "\n\n" + method_text
        return self.agent.run(prompt)

