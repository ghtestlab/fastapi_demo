from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI() # 创建 api 对象

class Item(BaseModel):
    cmd:str

@app.post('/')
def fileDowm(item:Item):  #把传过来的字典交给Item进行解析，若解析不正确返回422请求格式错误。
    '''
    文件下载模块
    :param item: {'cmd'：url}
    :return: filestream 字节流
    '''
    url=item.dict()['cmd']

    with open(url,'rb') as f:
        filestream=f.read()				#二进制读取文件
        import base64						
        filestream=base64.b64encode(filestream)    #转化为字节流进行文件传输
        
    return filestream


if __name__ == '__main__':
    uvicorn.run('main:app',port=8000)