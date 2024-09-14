from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/teste2")
def read_root():
    return {"teste2": "teste2"}

@app.get("/teste3")
def read_root():
    return {"teste3": "teste3"}

@app.get("/teste4")
def read_root():
    return {"teste4": "teste4"}