from utils.base_writer import BaseWriter


class ConsoleWriter(BaseWriter):
    """
    Writer for console output.

    Outputs the explanation directly to the console.
    """

    def write(self, explanation: str):
        """
        Print the explanation to the console.

        Args:
            explanation (str): The explanation to display.
        """
        print(f"🧙 {explanation}")
