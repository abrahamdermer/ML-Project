import pandas as pd
from fanctions.nb_Trainer import NBTrainer
from fanctions.create_data_frame_from_CSV import CreateDataFrame
from fanctions.menu import Meun
from fanctions.cleane_data_frame import CleaneDF
from fanctions.nb_Classifier import NBClassifier
from fanctions.test import Test


class Maneger:
    # _instance = None

    # def __new__(cls,adress,target):
    #     if not cls._instance:
    #         cls._instance = super().__new__(cls)
    #         cls._instance._init_(adress,target)
    #     return cls._instance


    def __init__(self,adress:str,target:str|None=None)-> None:
        self._df = CreateDataFrame.creat_df_from_adrrres(adress)
        self._cleane_df = None
        self._target = target
        self._traine = None
        self._test = None

    def run(self)->None:
        self._cleane_df = CleaneDF.cleane_df(self._df)
        self._traine = NBTrainer.trainer(self._cleane_df,self._target)

    def run_and_test(self)->None:
        self._cleane_df = CleaneDF.cleane_df(self._df)
        lern_df = None
        test_df = None
        self._traine = NBTrainer.trainer(lern_df,self._target)
        self._test = Test.get_test(self._traine,test_df,self._target)

    def get_classifi(self,promt:dict) -> str:
        return NBClassifier.classifier(self._traine,promt)
    
    def get_tast(self):
        if self._test:
            return self._test
        return None