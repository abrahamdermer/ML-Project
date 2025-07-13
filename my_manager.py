from fanctions.nb_Trainer import NBTrainer
from fanctions.create_data_frame_from_CSV import CreateDataFrame
from fanctions.cleane_data_frame import CleaneDF
from fanctions.nb_Classifier import NBClassifier
from fanctions.test import Test


class Manager:

    def __init__(self,adress:str,target:str|None=None)-> None:
        self._df = CreateDataFrame.creat_df_from_adrrres(adress)
        self._cleane_df = None
        self._target = target
        self._traine = None
        self._test = None

    def cline_data(self)->None:
        self._cleane_df = CleaneDF.cleane_df(self._df)

    def run(self)->None:
        self.cline_data()
        self._traine = NBTrainer.trainer(self._cleane_df,self._target)

    def run_and_test(self)->None:
        self.cline_data()
        test_df = self._cleane_df.sample(frac=0.3 , random_state=42)
        lern_df =self._cleane_df.drop(test_df.index)
        self._traine = NBTrainer.trainer(lern_df,self._target)
        self._test = Test.get_test(self._traine,test_df,self._target)

    def get_classifi(self,promt:dict) -> str:
        return NBClassifier.classifier(self._traine,promt)
        
    def get_test(self)->float|None:
        if self._test:
            return self._test
        return None
    
    def get_traine(self):
        if self._traine:
            return self._traine