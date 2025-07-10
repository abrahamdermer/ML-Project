from fanctions.nb_Classifier import NBClassifier
import pandas as pd

class Test:

    def _row_to_dict(row,target:dict)->dict:
        exclude_cols = ['id',target]
        return {k: v for k, v in row.items() if k not in exclude_cols}

    @staticmethod
    def get_test(train,test_df:pd.DataFrame,target=None)->float:
        if target is None:
            target = test_df.columns[-1]
        test_df['dddddd'] = test_df.apply(lambda x:NBClassifier.classifier(train,Test._row_to_dict(x)))
        mask = test_df['dddddd'] == test_df[target]
        return 100 * mask.sum() / len(test_df)