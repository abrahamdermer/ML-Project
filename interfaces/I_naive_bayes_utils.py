from abc import ABC , abstractmethod

class INaiveBayesUtils(ABC):
    
    @staticmethod
    @abstractmethod
    def build_naive_bayes(data,target) -> dict:
        pass