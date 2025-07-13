from fanctions.nb_Classifier import NBClassifier
import pandas as pd

class Test:
    @staticmethod
    def _row_to_dict(row,target:dict)->dict:
        exclude_cols = ['id',target]
        return {k: v for k, v in row.items() if k not in exclude_cols}

    @staticmethod
    def get_test(train,test_df:pd.DataFrame,target=None)->float:
        if target is None:
            target = test_df.columns[-1]
        # print(target)
        test_df['prediction'] = test_df.apply(lambda x:NBClassifier.classifier(train,Test._row_to_dict(x,target)),axis=1)
        mask = test_df['prediction'] == test_df[target]
        # print(100 * mask.sum() / len(test_df))
        return 100 * mask.sum() / len(test_df)