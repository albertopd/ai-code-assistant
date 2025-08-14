from utils.base_writer import BaseWriter


class TextFileWriter(BaseWriter):
    """
    Writer for outputting explanations to a text file.
    """

    def __init__(self, output_file: str):
        """
        Initialize the TextFileWriter with the output file path.

        Args:
            output_file (str): Path to the file where the explanation will be written.
        """
        self.output_file = output_file

    def write(self, explanation: str):
        """
        Write the explanation to the output file and print a confirmation message.

        Args:
            explanation (str): The explanation to write to the file.
        """
        with open(self.output_file, "w", encoding="utf-8") as f:
            f.write(explanation)

        print(f"💾 Explanation saved to: {self.output_file}\n")
