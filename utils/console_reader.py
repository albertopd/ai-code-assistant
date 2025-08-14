from typing import Tuple
from utils.base_reader import BaseReader


class ConsoleReader(BaseReader):
    """
    Reader for manual console input.

    Prompts the user to enter an error message and a code snippet interactively.
    """

    def read(self) -> Tuple[str, str]:
        """
        Prompt the user for an error message and code snippet via the console.

        Returns:
            Tuple[str, str]: The code snippet and the error message entered by the user.
        """
        error = input("🛑 Enter the error message (leave blank for the AI to infer):\n")
        print("\n🧾 Enter the code snippet (end with a blankline):")

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