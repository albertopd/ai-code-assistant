import os
from typing import Tuple
from utils.base_reader import BaseReader

class FileReader(BaseReader):

    ERROR_TAG = "[ERROR]"

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self) -> Tuple[str, str]:
        """
        Reads a code file and extracts an error message from the first line 
        if it contains the [ERROR] tag.

        Returns:
            Tuple (code, error) where:
                - code: string containing the source code (without error line)
                - error: string containing the extracted error message, or None
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

        # Remove the first line only if it contained an error message
        code = "".join(lines[1:]) if error else "".join(lines)

        return code, error