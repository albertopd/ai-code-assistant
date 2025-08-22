from abc import ABC, abstractmethod

class BaseWriter(ABC):
    """
    Abstract base class for output writers.

    Subclasses must implement the write() method to handle output of explanations.
    """

    @abstractmethod
    def write(self, explanation: str):
        """
        Output the explanation string to the desired destination.

        Args:
            explanation (str): The explanation to output.
        """
        ...