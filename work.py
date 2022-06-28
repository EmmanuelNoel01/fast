from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel  




app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str]=None


class UpdateItem(BaseModel):
     name:Optional[str]=None
     price:Optional[float]=None
     brand:Optional[str]=None

inventory ={
    1: {
        "name":"Milk",
        "price":3.99,
        "brand":"regular"
    }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]



@app.post("/create_item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return{"Error":"Item already exists."} 
    
    inventory[item_id]=item
    
    return inventory[item_id]


@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return{"error":"doesnt exist"}
    
    if item.name != None:
        inventory[item_id].name =item.name
        
    if item.price != None:
        inventory[item_id].name =item.price
        
    if item.brand != None:
        inventory[item_id].name =item.brand       
    
    return inventory[item_id]    
    
    
@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int):
    if item_id not in inventory:
        return{"error":"item doesnot exist"}
    del inventory[item_id]
    return{"success"}
        
    
    
        
       
       
# @app.post("/create-item/{item_id}")
# def create_item(item_id: int, item: Item):
#     if item_id in inventory:
#         return{"Error":"item already there"}
    
#     inventory[item_id]= item
#     return inventory[item_id]
              