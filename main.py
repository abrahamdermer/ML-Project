import pandas as pd
from maneger import Maneger
from fanctions.nb_Trainer import NBTrainer
from fanctions.create_data_frame_from_CSV import CreateDataFrame
from fanctions.menu import Meun
from fanctions.cleane_data_frame import CleaneDF
from fanctions.nb_Classifier import NBClassifier


# def has_zeros(dic:dict)->bool:
#     return any([i==0 for i in dic.values()])
    
# def add_one(dic: dict) -> None:
#     for k in dic:
#         dic[k] += 1

# def divider(dic:dict,num:int)-> None:
#     if num == 0:
#         return
#     if has_zeros(dic):
#         add_one(dic)
#         num += len(dic)
#     for k in dic.keys():
#         dic[k] /=num


# def build_probability_table(data:str,target:str=None)->dict:
#     df = pd.read_csv(data,sep=r'\s+')
#     # print(df.columns)
#     if not target or target not in df.columns:
#         target = df.columns[-1]
#     dic = {}
#     uniq_tar = df[target].unique()
#     columns = [col for col in df.columns if col not in [target,'id']]
#     for tar in uniq_tar:
#         ter_dict ={}
#         tar_count = len(df[df[target] == tar])
#         for col in columns:
#             uniq_val = df[col].unique()
#             col_dict = {}
#             for val in uniq_val:
#                 num = len(df[(df[target] == tar) & (df[col] == val)])
#                 col_dict[val] = num
#             divider(col_dict,tar_count)
#             ter_dict[col] = col_dict
#         dic[tar] = ter_dict
#     return dic

adress = "./data.csv"
# df = pd.read_csv("./data.csv",delim_whitespace=True)
# print(df.columns)
# print(df['age'].unique())


# def print_tabel(tabel:dict , distance  = 0)-> None:
#     for k in tabel.keys():
#         # print(distans)
#         print(f'{'    '*distance }{k}:')
#         if isinstance(tabel[k], dict):
#             print_tabel(tabel[k] , distance + 1)
#         else:
#             print(f"{'    '*(distance+1)}{tabel[k]}")

# print_tabel(aa('./data.csv','Buy_Computer'))

# df = CreateDataFrame.creat_df_from_adrrres('./data.csv')
# cleane_df = CleaneDF.cleane_df(df)
target = 'Buy_Computer'
# tabel = NBTrainer.trainer(cleane_df,target)
# print_tabel(tabel)
promt = {'age': 'youth', 'income':'high', 'student':'no', 'credit_rating':'excellent'}


# def predict_class1(tabel:dict,promt:dict)-> bool:
#     yes =  tabel['yes']['age'][promt['age']] * tabel['yes']['income'][promt['income']]*tabel['yes']['student'][promt['student']]*tabel['yes']['credit_rating'][promt['credit_rating']]
#     no = tabel['no']['age'][promt['age']]*tabel['no']['income'][promt['income']]*tabel['no']['student'][promt['student']]*tabel['no']['credit_rating'][promt['credit_rating']]
#     print({'no':no,'yes':yes})
#     return('no' if no > yes else 'yes')

# def predict_class(tabel:dict,promt:dict)-> bool:
#     dic ={}
#     for k in tabel.keys():
#         num = 1
#         for key,val in promt.items():
#             num *= tabel[k][key][val]
#         dic[k] = num
#     print(dic)
#     return max(dic , key=dic.get)
# res = NBClassifier.Classifier(tabel,promt)
# print(res)
# Meun.meun()
# exclude_cols = ['id',target]

# def row_to_dict(row):
#     dic = {k: v for k, v in row.items() if k not in exclude_cols}
#     print(dic)
#     return dic

# df['dddddd'] = df.apply(lambda x:NBClassifier.Classifier(tabel,row_to_dict(x)),axis=1)
# print(df)
# mask = df['dddddd'] == df[target]
# percent_diff = 100 * mask.sum() / len(df)
# print(f"{percent_diff} %")


meneger = Maneger(adress,target)
meneger.run()
print(f"for your promt the anser is: {meneger.get_classifi(promt)}, by {meneger.get_tast()}%")
