from fastapi import FastAPI

app = FastAPI()

#define root directory
@app.get("/")
def root():
    return {"Hello": "World!"}

#send items 
items = []

@app.post("/items")
def create_item(item:str):
    items.append(item)
    return {"updated item list": items}
#use to test>> curl -X POST -H "Content-Type:application/json" 'http://127.0.0.1:8000/items?item=example_item'  ❌
#use to test>> Invoke-WebRequest -Uri "http://127.0.0.1:8000/items?item=Apple" -Method POST -Headers @{ "Content-Type"="application/json" }
