import os
from functions.nb_Classifier import NBClassifier
import requests
import json


class Manager():


    @staticmethod
    def get_host():
        # בדיקה פשוטה - קיים קובץ של Docker
        if os.path.exists('/.dockerenv'):
            return "host.docker.internal"
        else:
            return "localhost"
        

    def __init__(self,address:str = f"http://{get_host()}:8000/"):
        req = requests.get(address)
        self._triner = req.json()
        # print(type(self._triner))
        # print(self._triner)


    def get_classifi(self,promt:dict) -> str:
        return NBClassifier.classifier(self._triner,promt)


