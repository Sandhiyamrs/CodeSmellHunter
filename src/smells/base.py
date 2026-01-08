from abc import ABC, abstractmethod

class CodeSmell(ABC):
    name = ""
    severity = "MEDIUM"

    @abstractmethod
    def detect(self, tree, filename):
        pass
