from fastapi import FastAPI, Request
import os
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
key=os.getenv("OPENAI_API_KEY")
print("dotenv key:",key)
app=FastAPI()

# schema
class Item(BaseModel):
    name:str
    price:float
    age:int
    message:str



@app.get("/")
def read_root():
    return {"Hello there!"}

@app.get("/items/{item_id}")
def read_item(item_id:int,q:str | None=None):
    return {"item_id":item_id,"q":q}

@app.put("/items/{item_id}")
def update_item(item_id:int,item:Item):
    return{"item_name:",item.name,"item_id:",item_id}

@app.get("/search")
def search(q:str):
    return {
        "query":q
    }

@app.post("/chat")
async def chat(request:Item):
    return {
        "message":request.message
    }