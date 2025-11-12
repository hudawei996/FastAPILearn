import uvicorn
from fastapi import FastAPI

app = FastAPI()


# 如果这里有参数，URL则必须携带参数才能访问成功
# 如：http://127.0.0.1:8000/query1?page=1&limit=100 正确返回
# 如：http://127.0.0.1:8000/query1  会报错
@app.get("/query1")
def page_limit(page, limit):
    return {"page": page, "limit": limit}


@app.get("/query2")
def page_limit2(page: int, limit=None):
    if limit is None:
        return {"page": page, "limit": 20}
    return {"page": page, "limit": limit}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
