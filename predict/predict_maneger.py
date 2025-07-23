from functions.nb_Classifier import NBClassifier
import requests
import json


class Manager():
    def __init__(self,address:str = 'http://host.docker.internal:8000/'):
        req = requests.get(address)
        self._triner = req.json()
        # print(type(self._triner))
        # print(self._triner)


    def get_classifi(self,promt:dict) -> str:
        return NBClassifier.classifier(self._triner,promt)


