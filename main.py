import pandas as pd
from fanctions.naive_bayes_utils import NaiveBayesUtils

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

# df = pd.read_csv("./data.csv",delim_whitespace=True)
# print(df.columns)
# print(df['age'].unique())
def print_tabel(tabel:dict , distance  = 0)-> None:
    for k in tabel.keys():
        # print(distans)
        print(f'{'    '*distance }{k}:')
        if isinstance(tabel[k], dict):
            print_tabel(tabel[k] , distance + 1)
        else:
            print(f"{'    '*(distance+1)}{tabel[k]}")
# print_tabel(aa('./data.csv','Buy_Computer'))

tabel = NaiveBayesUtils.build_probability_table('./data.csv','Buy_Computer')
promt = {'age': 'youth', 'income':'high', 'student':'no', 'credit_rating':'excellent'}
def predict_class1(tabel:dict,promt:dict)-> bool:
    yes =  tabel['yes']['age'][promt['age']] * tabel['yes']['income'][promt['income']]*tabel['yes']['student'][promt['student']]*tabel['yes']['credit_rating'][promt['credit_rating']]
    no = tabel['no']['age'][promt['age']]*tabel['no']['income'][promt['income']]*tabel['no']['student'][promt['student']]*tabel['no']['credit_rating'][promt['credit_rating']]
    print({'no':no,'yes':yes})
    return('no' if no > yes else 'yes')

def predict_class(tabel:dict,promt:dict)-> bool:
    dic ={}
    for k in tabel.keys():
        num = 1
        for key,val in promt.items():
            num *= tabel[k][key][val]
        dic[k] = num
    print(dic)
    return max(dic , key=dic.get)

print(predict_class(tabel,promt))
print(predict_class1(tabel,promt))