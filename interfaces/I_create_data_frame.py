from abc import ABC , abstractmethod
import pandas as pd


class ICreateDataFrame(ABC):

    @staticmethod
    @abstractmethod
    def creat_df_from_adrrres(adrres:str) -> pd.DataFrame:
        pass