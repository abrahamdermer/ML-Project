from typing import Union
from my_manager import Manager

from fastapi import FastAPI

app = FastAPI()

target = 'class'
adress = "./newqq.csv"
# יצירת מופע של מנהל
manager = Manager(adress,target)
manager.run_and_test()


@app.get("/")
def read_root():
    return manager.get_traine()
