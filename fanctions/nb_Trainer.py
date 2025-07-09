import pandas as pd
from interfaces.I_Trainer import ITrainer


class NaiveBayesUtils(ITrainer):

    @staticmethod   
    def _has_zeros(dic:dict)->bool:
        return any([i==0 for i in dic.values()])
    
    @staticmethod    
    def _add_one(dic: dict) -> None:
        for k in dic:
            dic[k] += 1
            
    @staticmethod
    def _divider(dic:dict,num:int)-> None:
        if num == 0:
            return
        if NaiveBayesUtils._has_zeros(dic):
            NaiveBayesUtils._add_one(dic)
            num += len(dic)
        for k in dic.keys():
            dic[k] /=num

    @staticmethod
    def trainer(df:pd.DataFrame,target:str=None)->dict:
        if not target or target not in df.columns:
            target = df.columns[-1]
        dic = {}
        uniq_tar = df[target].unique()
        columns = [col for col in df.columns if col not in [target,'id']]
        for tar in uniq_tar:
            ter_dict ={}
            tar_count = len(df[df[target] == tar])
            for col in columns:
                uniq_val = df[col].unique()
                col_dict = {}
                for val in uniq_val:
                    num = len(df[(df[target] == tar) & (df[col] == val)])
                    col_dict[val] = num
                NaiveBayesUtils._divider(col_dict,tar_count)
                ter_dict[col] = col_dict
            dic[tar] = ter_dict
        return dic
    