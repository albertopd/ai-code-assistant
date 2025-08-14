import os
from typing import Tuple
from utils.base_reader import BaseReader


class TextFileReader(BaseReader):
    """
    Reader for text/code files. Extracts code and error message from files.
    """

    ERROR_TAG = "[ERROR]"

    def __init__(self, file_path: str):
        """
        Initialize the TextFileReader with the path to the file.

        Args:
            file_path (str): Path to the code or text file to read.
        """
        self.file_path = file_path

    def read(self) -> Tuple[str, str]:
        """
        Read the file and extract the code and error message.

        If the first line contains the [ERROR] tag, the error message is extracted
        and the rest of the file is treated as code. Otherwise, the entire file is
        treated as code and error is set to an empty string.

        Returns:
            Tuple[str, str]:
                - code: The code snippet (excluding the error line if present).
                - error: The extracted error message, or an empty string if not found.
        """
        if not os.path.isfile(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

        with open(self.file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        if not lines:
            return "", ""

        first_line = lines[0].strip()
        error = ""

        # Look for the error tag anywhere in the first line
        if self.ERROR_TAG in first_line:
            # Get everything after the tag
            error = first_line.split(self.ERROR_TAG, 1)[1].strip()

            print(f"🛑 Extracted error message => {error}\n")

        # Remove the first line only if it contained an error message
        code = "".join(lines[1:]) if error else "".join(lines)

        return code, error
