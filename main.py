import uvicorn

# adress = "./data.csv"
# target = 'Buy_Computer'
# promt = {'age': 'youth', 'income':'high', 'student':'no', 'credit_rating':'excellent'}

if __name__ == '__main__':
    uvicorn.run("API:app", host="0.0.0.0", port=8000, reload=True)