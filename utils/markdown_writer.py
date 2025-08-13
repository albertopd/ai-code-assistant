from utils.base_writer import BaseWriter

class MarkdownWriter(BaseWriter):
    def __init__(self, output_file: str):
        self.output_file = output_file

    def write(self, explanation: str):
        with open(self.output_file, "w", encoding="utf-8") as f:
            f.write(explanation)
        print(f"Explanation written to {self.output_file}")