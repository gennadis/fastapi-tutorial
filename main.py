from pydantic import BaseModel

from fastapi import FastAPI, Query

api = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@api.get("/")
async def root():
    return {"message": "Hello, world"}


@api.get("/items/{item_id}")
async def read_item(item_id: int, needy: str, skip: int, limit: int | None = None):
    return {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}


@api.get("/users/me")
async def read_user_me():
    return {"user": "the current user"}


@api.get("/users/{user_ud}")
async def read_user(user_id: int):
    return {"user": user_id}


@api.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@api.get("/items/")
async def read_items(
    q: list[int]
    | None = Query(
        default=[1, 3, 1999],
        title="List of integers",
        description="List of integers",
        deprecated=True,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
