from fastapi import APIRouter
from pydantic import BaseModel
from typing import Union
from config import database


class ItemDetail(BaseModel):
    item_color: str
    item_detail: str


class Item2(BaseModel):
    item_id: Union[int, str]
    item_name: str
    item_bool: bool
    item_detail: ItemDetail


class Item(BaseModel):
    item_id: Union[int, str]
    item_name: str
    item_bool: bool


router = APIRouter(prefix="/items", tags=["items"])
cur = database.client["exceed06"]["testDB"]


@router.get("/{item_id}/{item_name}/{item_bool}")
def show_item(item_id: Union[int, str], item_name: str, item_bool: bool):
    filter = {"_id": 0}
    t = list(
        cur.find(
            {"item_id": item_id, "item_name": item_name, "item_bool": item_bool}, filter
        )
    )
    return t


@router.post("/add", status_code=201)
def create_item(item_id: Union[int, str], item_name: str, item_bool: bool):
    if not cur.find_one({"item_id": item_id}):
        cur.insert_one(
            {"item_id": item_id, "item_name": item_name, "item_bool": item_bool}
        )
        return {"status": "suscess"}
    else:
        return {"status": "already"}
