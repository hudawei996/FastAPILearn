import uvicorn
from aiohttp.web_exceptions import HTTPException
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# 需求：新闻接口 → 响应数据格式 id、title、content
class News(BaseModel):
    id: int
    title: str
    content: str


@app.get("/news/{id}")
async def get_news(id: int):
    id_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if id not in id_list:
        raise HTTPException(status_code=404, detail="新闻不存在")

    return {
        "id": id,
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
