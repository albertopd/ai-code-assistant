from abc import ABC, abstractmethod

class BaseWriter(ABC):
    @abstractmethod
    def write(self, explanation: str):
        pass