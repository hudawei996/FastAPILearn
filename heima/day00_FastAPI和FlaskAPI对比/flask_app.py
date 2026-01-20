import asyncio
import time

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/sync')
def func_sync():
    start = time.time()
    for i in range(10):
        time.sleep(1)
    end = time.time()
    return {"time": f'{(end - start):.2f}s'}

@app.route('/async')
async def func_async():
    start = time.time()
    tasks = [asyncio.sleep(1) for i in range(10)]
    await asyncio.gather(*tasks)
    end = time.time()
    return {"time": f'{(end - start):.2f}s'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)