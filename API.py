from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from my_manager import Manager
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")


app = FastAPI()

target = 'class'
adress = "./newqq.csv"
manager = Manager(adress,target)
manager.run_and_test()
# manager.run()



@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    trained_data = manager.get_traine()  # שליפת המילון מה-Manager
    features = {}
    
    for category in trained_data["e"]:  # עבור כל קטגוריה ב-"e"
        if isinstance(trained_data["e"][category], dict):
            # יצירת מבנה נתונים מורחב עם תוויות ותיאורים
            features[category] = {
                "label": category,  # ניתן להחליף לשמות יותר ידידותיים
                "description": "בחר את האפשרות המתאימה",  # ניתן להתאים תיאורים ספציפיים
                "options": [{"value": k, "label": k} for k in trained_data["e"][category].keys()]
            }
    
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "features": features}
    )


@app.post("/classifi/")
def send(promt:dict):
    print(promt)
    promt = dict(promt)
    return manager.get_classifi(promt)

@app.get("/test")
def test():
    return manager.get_test()

@app.get("/options")
def op():
    return manager.get_traine()