import pandas as pd
from interfaces.I_Trainer import ITrainer


class NBTrainer(ITrainer):

    @staticmethod   
    def _has_zeros(dic:dict)->bool:
        return any(i==0 for i in dic.values())
    
    @staticmethod    
    def _add_one(dic: dict) -> None:
        for k in dic:
            dic[k] += 1
            
    @staticmethod
    def _divider(dic:dict,num:int)-> None:
        if num == 0:
            return
        if NBTrainer._has_zeros(dic):
            NBTrainer._add_one(dic)
            num += len(dic)
        for k in dic.keys():
            dic[k] /=num

    @staticmethod
    def _tar_present(dic:dict) -> None:
        flag = int(any(val['tar_presnt'] == 0 for val in dic.values()))
        count = sum(dic[key]['tar_presnt'] for key in dic.keys())
        if flag:
            count += len(dic)
        for val in dic.values():
            val['tar_presnt'] = (val['tar_presnt'] + flag) /count

    @staticmethod
    def trainer(df:pd.DataFrame,target:str=None)->dict:
        if not target or target not in df.columns:
            target = df.columns[-1]
        dic = {}
        uniq_tar = df[target].unique()
        columns = [col for col in df.columns if col not in [target,'id']]
        for tar in uniq_tar:
            tar_dict ={}
            tar_count = len(df[df[target] == tar])
            for col in columns:
                uniq_val = df[col].unique()
                col_dict = {}
                for val in uniq_val:
                    num = len(df[(df[target] == tar) & (df[col] == val)])
                    col_dict[val] = num
                NBTrainer._divider(col_dict,tar_count)
                tar_dict[col] = col_dict
            tar_dict['tar_presnt'] = tar_count
            dic[tar] = tar_dict
        NBTrainer._tar_present(dic) 
        return dic
    