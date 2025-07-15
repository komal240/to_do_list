from fastapi import FastAPI
from databse import query
from pydantic import BaseModel
app=FastAPI()

class addItemModel(BaseModel):
    to_do:str

class deleteItemModel(BaseModel):
    id:int  

#display all items
@app.get("/display_all")
def display_all():
    result=query("SELECT *FROM list")
    return result

#add items
@app.post("/add")
def add(item:addItemModel):
    print(item)
    result=query(f"INSERT INTO list (to_do)VALUES('{item.to_do}')" )
    return("success")

#delete item
@app.post("/delete")
def delete(item:deleteItemModel):
    result=query(f"DELETE FROM list WHERE id='{item.id}'")
    return ("delete item")

    