from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    command: str


app = FastAPI()

#@app.put("/items/{item_id}")
@app.post("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    if item_id == 0:
        return {"item_id": item_id, **item.dict()}
    else:        
        return {"item_id": item_id, **item.dict()}