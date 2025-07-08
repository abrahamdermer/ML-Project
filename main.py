import pandas as pd

def has_zeros(dic:dict)->bool:
    flag = sum([i==0 for i in dic.values()])
    if flag:
        for k in dic.keys():
            dic[k]+=1
        return True
    return False

def divider(dic:dict,num:int)-> None:
    if num == 0:
        return
    num += int(has_zeros(dic))
    for k in dic.keys():
        dic[k] /=num


def aa(data:str,target:str)->dict:
    df = pd.read_csv(data,delim_whitespace=True)
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
            divider(col_dict,tar_count)
            ter_dict[col] = col_dict
        dic[tar] = ter_dict
    return dic

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
print_tabel(aa('./data.csv','Buy_Computer'))
