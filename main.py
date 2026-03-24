from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi import HTTPException


class Item(BaseModel):
    name: str = Field(min_length=1)

app = FastAPI()

items = {}
current_id = 1

@app.get("/items")
async def get_all_items():
    return [{"id": item_id, **data} for item_id, data in sorted(items.items())]

@app.get("/items/{item_id}")
async def get_item_by_id(item_id: int):
    if item_id in items:
        return {"id": item_id, **items[item_id]}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items")
async def save_items(item: Item):
    global current_id
    item_dict = item.model_dump()
    nuevo_id = current_id
    current_id += 1
    items[nuevo_id] = item_dict
    return {"id": nuevo_id, **item_dict}
