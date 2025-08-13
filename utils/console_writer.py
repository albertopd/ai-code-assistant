from utils.base_writer import BaseWriter

class ConsoleWriter(BaseWriter):
    def write(self, explanation: str):
        print(explanation)