from typing import Union #联合参数

from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel #从 pydantic 中导入 BaseModel：
 
import uvicorn

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

# 用在post请求中
class Item(BaseModel):
    name: str
    description: Union[str, None] = None #使用联合参数，定义为可选参数
    price: float
    tax: Union[float, None] = None

app = FastAPI()

@app.get("/demo")
async def root():
    return {"message":"hello word"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}


#路径转换器
@app.get("/file/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# 请求体，使用postf发送请求体
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# 请求体 + 路径参数
@app.post("/items/{item_id}")
async def create_item(item_id:int, item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
        item_dict.update({"item_id": item_id})
    return item_dict


@app.put("/items/{items_id}")
async def create(item: Item, items_id: int, q: Union[str,None] = None):
    item_dict = item_dict.dict()
    result = {"item_id": items_id, **item.dict()}
    if q:
        result.update("q", q)
    return result


# 请求体 + 路径参数 + 查询参数


# 交互式API文档：http://127.0.0.1:8000/docs，可做api调试平台


# if __name__ == '__main__':
#     uvicorn.run('demo:app',port=8000)
#     # uvicorn main:app --reload

