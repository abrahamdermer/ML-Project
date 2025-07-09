import nb_lassifier
import pandas as pd
target = ''
exclude_cols = ['id',target]

def row_to_dict(row):
    return {k: v for k, v in row.items() if k not in exclude_cols}


df = pd.read_csv('./data.csv')
df['dddddd'] = df.apply(lambda x:nb_lassifier(row_to_dict(x)))
print(df)