from agents import experiment_agent
from utils import pdf_loader
from utils.pdf_loader import PDFLoader
from agents.parser_agent import ParserAgent
from agents.method_agent import MethodAgent
from agents.experiment_agent import ExperimentAgent
import argparse

def main(pdf_path):

    base_name = pdf_path[:-4] 

    pdf_loader = PDFLoader()

    text = pdf_loader.load_pdf_text(pdf_path)

    with open(f"outputs/text/{base_name}_text.txt", "w") as f:
        f.write(text)

    parser_agent = ParserAgent()
    parsed = parser_agent.parse_paper(text)
    with open(f"outputs/parsed/{base_name}_parsed.txt", "w") as f:
        f.write(parsed)

    method_agent = MethodAgent()
    method = method_agent.extract_method(parsed)
    with open(f"outputs/method/{base_name}_method.txt", "w") as f:
        f.write(method)

    experiment_agent = ExperimentAgent()
    experiment = experiment_agent.design_experiment(method)

    with open(f"outputs/experiment/{base_name}_experiment.txt", "w") as f:
        f.write(experiment)
if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Run paper → method → experiment agent pipeline"
    )
    parser.add_argument(
        "pdf_path",
        type=str,
        help="Path to the research paper PDF"
    )

    args = parser.parse_args()
    main(args.pdf_path)