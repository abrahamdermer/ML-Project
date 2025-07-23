from abc import ABC,abstractmethod

# Abstract base class for classifiers
class IClassifier(ABC):

# Abstract method for classification
    @staticmethod
    @abstractmethod
    def classifier(tabel:dict,promt:dict) -> str:
        pass