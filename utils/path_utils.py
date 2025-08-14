import os
from pathlib import Path


def generate_output_file_path(
    input_file_path: str, 
    output_file_ext: str,
    output_dir: str,
) -> str:
    """
    Generate the output file path based on the name of the input file and the output directory.

    Args:
        input_path (str): The path to the input code file.
        output_file_ext (str): The file extension for the output file.
        output_dir (str): The output directory for the generated file path.

    Returns:
        str: The path to the output file in the output directory.
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    base_name = Path(input_file_path).stem
    output_file_path = f"{base_name}.{output_file_ext.lstrip('.')}"

    return os.path.join(output_dir, output_file_path)