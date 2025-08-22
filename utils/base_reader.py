from abc import ABC, abstractmethod
from typing import Tuple

class BaseReader(ABC):
    """
    Abstract base class for input readers.

    Subclasses must implement the read() method to return a tuple containing
    the code snippet and the error message.
    """

    @abstractmethod
    def read(self) -> Tuple[str, str]:
        """
        Read input and return a tuple of (code, error).

        Returns:
            Tuple[str, str]: The code snippet and the error message.
        """
        ...