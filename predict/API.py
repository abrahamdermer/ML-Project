from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from predict_maneger import Manager


templates = Jinja2Templates(directory="templates")


app = FastAPI()

# Create a Manager object
manager = Manager()

# Get the prompt from the request and return the classification.
@app.get("/classifi/")
def send(promt:dict):
    promt = dict(promt)
    return manager.get_classifi(promt)