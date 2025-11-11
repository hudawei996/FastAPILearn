# 第一个fastapi程序
import uvicorn
from fastapi import FastAPI

app01 = FastAPI()


# 根服务
@app01.get("/")
def read_root():
    return {"Hello": "World123"}


# 启动服务
# 1.通过命令：uvicorn filename:app_name --reload
# 1.通过命令：uvicorn main01:app01 --reload # 启动服务，并自动重新加载代码内容
# 2.通过调试：fastapi dev filename # 需要安装fastapi[standard]
# 3.通过py运行：python filename.py (需要下边的代码才能运行，否则什么也不会有）
if __name__ == "__main__":
    # uvicorn.run("main01:app01", host="127.0.0.1", port=8000, reload=True)
    uvicorn.run(app01, host="127.0.0.1", port=8000)
