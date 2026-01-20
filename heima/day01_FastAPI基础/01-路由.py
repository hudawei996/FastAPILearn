import uvicorn
from fastapi import FastAPI

# 创建 FastAPI 实例
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World666"}


# 访问 /hello  响应结果 msg: 你好 FastAPI
@app.get("/hello/{name}")
async def get_hello(name:str):
    return {"msg": f"你好 FastAPI {name}"}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)