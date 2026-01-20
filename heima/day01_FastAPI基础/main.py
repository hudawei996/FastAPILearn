import asyncio
import time

import uvicorn
from fastapi import FastAPI

# 00-同异步耗时对比

app = FastAPI()

# 同步耗时
@app.get("/sync")
def func_sync():
    start = time.time()

    for i in range(10):
        time.sleep(1)

    end = time.time()
    return {"time": f'{end - start:.2f}s'}

# 异步耗时
@app.get("/async")
async def func_async():
    start = time.time()

    tasks = [asyncio.sleep(1) for i in range(10)]
    await asyncio.gather(*tasks)
    # for i in range(10):
    #     time.sleep(1)

    end = time.time()
    return {"time": f'{end - start:.2f}s'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)