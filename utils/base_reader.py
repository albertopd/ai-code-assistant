from abc import ABC, abstractmethod
from typing import Tuple

class BaseReader(ABC):
    @abstractmethod
    def read(self) -> Tuple[str, str]:
        pass