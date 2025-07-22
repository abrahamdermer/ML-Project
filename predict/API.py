from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.templating import Jinja2Templates
from predict_maneger import Manager


templates = Jinja2Templates(directory="templates")


app = FastAPI()

# יצירת מופע של מנהל
manager = Manager()
print("manager ")



# שליחת טופס ספציפי של פיטריות
# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
    # trained_data = manager._triner  # שליפת המילון מהמנהל
    # features = {}

    # for category in trained_data["e"]:  # עבור כל קטגוריה ב-"e"
    #     if isinstance(trained_data["e"][category], dict):
    #         # יצירת מבנה נתונים מורחב עם תוויות ותיאורים
    #         features[category] = {
    #             "label": category,  # ניתן להחליף לשמות יותר ידידותיים
    #             "description": "בחר את האפשרות המתאימה",  # ניתן להתאים תיאורים ספציפיים
    #             "options": [{"value": k, "label": k} for k in trained_data["e"][category].keys()]
    #         }
    
    # 
    # return {'aaa':'aaaaa'}

# קבלת ה"פרומט" מהמשתנה
@app.post("/classifi/")
def send(promt:dict):
    print(promt)
    promt = dict(promt)
    return manager.get_classifi(promt)

# החזרת אחוזי הדיוק
@app.get("/test")
def test():
    return manager.get_test()

# # זה מחזיר את המסווג שיוכלו  לראות את הסוגים
# @app.get("/options")
# def op():
#     return manager.get_traine()