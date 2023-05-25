# from fastapi import FastAPI
# import uvicorn

# app = FastAPI() # 创建 api 对象

# @app.get("/") # 配置路由
# def root():
#     return {"test01": "1111"}

# # async def root():
# #     return {"test01": "1111"}


# if __name__ == '__main__':
#     uvicorn.run('test:app',port=8000) #main：py文件名 app：api对象名


from typing import Union

from fastapi import FastAPI
#from fastapi.exceptions import MalformedRequest
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'))

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}