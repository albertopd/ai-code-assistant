from typing import Tuple
from utils.base_reader import BaseReader

class ConsoleReader(BaseReader):
    def read(self) -> Tuple[str, str]:
        error = input("\nEnter the error message:\n")
        code = input("\nEnter the code snippet (end with a blankline):\n")
        lines = []
        while True:
            try:
                line = input()
                if line.strip() == "":  # stop on blank line
                    break
                lines.append(line)
            except EOFError:
                break
        code = "\n".join(lines)
        return (code, error)
