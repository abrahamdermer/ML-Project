from interfaces.I_classifier import IClassifier

class NBClassifier(IClassifier):

    @staticmethod
    def Classifier(tabel:dict,promt:dict)-> str:
        dic ={}
        for k in tabel.keys():
            num = 1
            for key,val in promt.items():
                num *= tabel[k][key][val]
            dic[k] = num
        print(dic)
        return max(dic , key=dic.get)