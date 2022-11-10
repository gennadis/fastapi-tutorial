from fastapi import FastAPI

api = FastAPI()


@api.get("/")
async def root():
    return {"message": "Hello, world"}


@api.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
