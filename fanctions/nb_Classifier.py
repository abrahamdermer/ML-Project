from interfaces.I_classifier import IClassifier

class NBClassifier(IClassifier):

    @staticmethod
    def classifier(tabel:dict,promt:dict)-> str:
        dic ={}
        colunms_num = 0
        for k in tabel.keys():
            num = 1
            for key,val in promt.items():
                num *= tabel[k][key][val]
            dic[k] = num*tabel[k]['tar_presnt']
        return max(dic , key=dic.get)