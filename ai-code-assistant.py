import os
import sys

from dotenv import load_dotenv
from utils.file_reader import FileReader
from utils.console_reader import ConsoleReader
from utils.console_writer import ConsoleWriter
from utils.llm_client import LlmClient
from utils.markdown_writer import MarkdownWriter


# Output folder for explanations
OUTPUT_DIR = os.path.join("data", "explanations")

def load_config() -> tuple[str, str]:
    """
    Loads environment variables from .env file and returns API_KEY and AI_MODEL.
    Raises an exception if required variables are missing.
    """
    load_dotenv()

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise Exception("GOOGLE_API_KEY not found. Please set it in your .env file.")
    
    ai_model = os.getenv("AI_MODEL")
    if not ai_model:
        raise Exception("AI_MODEL not found. Please set it in your .env file.")
    
    return api_key, ai_model

def generate_output_path(input_path: str) -> str:
    """
    Generates a markdown output file path in data/explanations
    based on the name of the input file (without extension).
    """
    # Ensure explanations directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_file = f"{base_name}.md"

    return os.path.join(OUTPUT_DIR, output_file)

def main():
    # Load configuration
    api_key, ai_model = load_config()

    # Initialize LLM client
    llm_client = LlmClient(api_key=api_key, ai_model=ai_model)

    # Check if a file path was passed as a parameter
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
        print(f"Input file: {input_file_path}")
        reader = FileReader(input_file_path)
        writer = MarkdownWriter(generate_output_path(input_file_path))
    else:
        print("No input file path provided, switching to manual input mode...")
        reader = ConsoleReader()
        writer = ConsoleWriter()

    code, error = reader.read()

    if not code.strip():
        print("Sorry can't do. No code snippet provided.")
        return

    if not error.strip():
        print("No error message provided. Will let the model check if there is any.")

    print("\nAnalyzing code...\n")
    explanation = llm_client.get_explanation(code, error)
    writer.write(explanation)


if __name__ == "__main__":
    main()
