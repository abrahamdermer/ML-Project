import os
from functions.nb_Classifier import NBClassifier
import requests
import json


class Manager():

# Return host address: "host.docker.internal" if in Docker, else "localhost".
    @staticmethod
    def get_host():
        if os.path.exists('/.dockerenv'):
            return "host.docker.internal"
        else:
            return "localhost"
        
# Constructor: creates a trainer field for all requests
    def __init__(self,address:str = f"http://{get_host()}:8000/"):
        req = requests.get(address)
        self._triner = req.json()

# Return the classification by parameters
    def get_classifi(self,promt:dict) -> str:
        return NBClassifier.classifier(self._triner,promt)


