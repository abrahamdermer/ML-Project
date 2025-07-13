from interfaces.I_create_data_frame import ICreateDataFrame
import pandas as pd


class CreateDataFrame(ICreateDataFrame):

    @staticmethod
    def creat_df_from_adrrres(adrres:str) -> pd.DataFrame:
        return pd.read_csv(adrres,sep=r'[,\s]+', engine='python')