import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    pwd:str | None
    sex:str = "男"


@app.post('/users')
def create_user(user:dict):
    return user


@app.post('/users2')
def create_user2(user:User):
    return user



if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port=8000)
    uvicorn.run('main05:app', host="127.0.0.1", port=8000, reload=True)