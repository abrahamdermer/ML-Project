from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.templating import Jinja2Templates
from predict_maneger import Manager


templates = Jinja2Templates(directory="templates")


app = FastAPI()

# # יצירת מופע של מנהל
# manager = Manager()
# print("manager ")

manager = Manager()

# קבלת ה"פרומט" מהמשתנה
@app.get("/classifi/")
def send(promt:dict):
    # global manager
    # if manager == '':
    #     manager = Manager()
    # return(promt)
    promt = dict(promt)
    return manager.get_classifi(promt)

# החזרת אחוזי הדיוק
# @app.get("/test")
# def test():
#     return manager.get_test()

# # זה מחזיר את המסווג שיוכלו  לראות את הסוגים
# @app.get("/options")
# def op():
#     return manager.get_traine()