from abc import ABC , abstractmethod

class ITrainer(ABC):
    
    @staticmethod
    @abstractmethod
    def trainer(data,target) -> dict:
        pass