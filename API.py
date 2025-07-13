from fastapi import FastAPI
from my_manager import Manager

app = FastAPI()

target = 'class'
adress = "./newqq.csv"
manager = Manager(adress,target)
manager.run_and_test()



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/classifi/")
def send(promt:dict):
    print(promt)
    promt = dict(promt)
    return manager.get_classifi(promt)

@app.get("/test")
def test():
    return manager.get_test()