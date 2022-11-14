from pydantic import BaseModel

from fastapi import FastAPI, Query, Path

api = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@api.get("/")
async def root():
    return {"message": "Hello, world"}


# @api.get("/items/{item_id}")
# async def read_item(item_id: int, needy: str, skip: int, limit: int | None = None):
#     return {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}


@api.get("/users/me")
async def read_user_me():
    return {"user": "the current user"}


@api.get("/users/{user_ud}")
async def read_user(user_id: int):
    return {"user": user_id}


@api.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@api.get("/items/{item_id}")
async def read_item(q: str, item_id: int = Path(title="ITEM ID", ge=1, le=10)):
    results = {"items": ["foo", "bar"], "things": ["bar", "foo"], "item_id": item_id}
    if q:
        results.update({"q": q})
    return results
