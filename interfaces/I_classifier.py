from abc import ABC,abstractmethod

class IClassifier(ABC):

    @staticmethod
    @abstractmethod
    def classifier(tabel:dict,promt:dict) -> str:
        pass