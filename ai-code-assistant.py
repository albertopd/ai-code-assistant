import argparse
import os
from pathlib import Path
import sys
from dotenv import load_dotenv
from utils.base_reader import BaseReader
from utils.base_writer import BaseWriter
from utils.console_reader import ConsoleReader
from utils.console_writer import ConsoleWriter
from utils.path_utils import generate_output_file_path
from utils.text_file_reader import TextFileReader
from utils.text_file_writer import TextFileWriter
from utils.llm_client import LlmClient


# Default Output folder for explanations
DEFAULT_OUTPUT_DIR = os.path.join("data", "explanations")
MARKDOWN_FILE_EXT = "md"


def load_config() -> tuple[str, str]:
    """
    Load API key and model name from the .env file.

    Returns:
        tuple[str, str]: A tuple containing the Google Gemini API key and model name.

    Raises:
        Exception: If either GOOGLE_API_KEY or AI_MODEL is missing in the environment.
    """
    load_dotenv()

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise Exception("GOOGLE_API_KEY not found. Please set it in your .env file.")

    ai_model = os.getenv("AI_MODEL")
    if not ai_model:
        raise Exception("AI_MODEL not found. Please set it in your .env file.")

    return api_key, ai_model

def get_arguments() -> tuple[str, str]:
    """
    Get command line arguments.

    Returns:
        tuple[str, str]: A tuple containing the input file path and output directory.
    """
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("input_file", nargs="?", help="Path to the code file")
    parser.add_argument(
        "-o",
        "--output-dir",
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for explanations",
    )
    args = parser.parse_args()

    return args.input_file, args.output_dir

def setup_io_handlers(
    input_file_path: str, 
    output_dir: str
) -> tuple[BaseReader, BaseWriter]:
    """
    Initialize and return the appropriate reader and writer
    based on whether an input file path is provided.

    If `input_file_path` is given, a TextFileReader is created
    to read the file, and a TextFileWriter is created to write
    the output to the specified directory. If not, the function
    switches to console-based input/output using ConsoleReader
    and ConsoleWriter.

    Args:
        input_file_path (str): Path to the input code file. If None or empty,
            console input mode is used instead.
        output_dir (str): Directory to save the output file when using
            file-based I/O.

    Returns:
        tuple[BaseReader, BaseWriter]: The initialized reader and writer instances.
    """
    if input_file_path:
        print(f"✨ Processing provided input file: {input_file_path}\n")
        reader = TextFileReader(input_file_path)
        writer = TextFileWriter(generate_output_file_path(input_file_path, MARKDOWN_FILE_EXT, output_dir))
    else:
        print("✍️  No input file provided, switching to manual input mode...\n")
        reader = ConsoleReader()
        writer = ConsoleWriter()

    return reader, writer

def main():
    """
    Main entry point for the AI Code Assistant.

    Loads configuration, initializes the LLM client, reads code and error input
    (from file or console), generates an explanation, and writes the output
    (to Markdown file or console).
    """
    input_file, output_dir = get_arguments()

    try:
        print("\n🤖 <<< Welcome to the AI Code Assistant >>>\n")

        api_key, ai_model = load_config()
        llm_client = LlmClient(api_key=api_key, ai_model=ai_model)

        reader, writer = setup_io_handlers(input_file, output_dir)
        code, error = reader.read()

        if not code.strip():
            print("[ERROR] No code snippet provided.")
            sys.exit(1)

        if not error.strip():
            print("🤔 No error message provided. But challenge accepted! I will find it myself. 🧐\n")

        print("🧠 Analyzing code...\n")
        explanation = llm_client.get_explanation(code, error)
        writer.write(explanation)

    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
