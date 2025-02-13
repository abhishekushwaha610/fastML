# app/routes/greeting.py
from fastapi import APIRouter, File,UploadFile
from starlette.requests import Request

router = APIRouter()


@router.post("/file")
def get_items(file: UploadFile = File(...)):
    print(file)
    return {"items": ["item1", "item2", "item3"]}
