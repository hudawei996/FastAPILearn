import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# 注册： 用户名和密码 → str
class User(BaseModel):
    username: str = Field(default="张三", min_length=2, max_length=10, description="用户名，长度要求2-10个字")
    password: str = Field(min_length=3, max_length=20)


@app.post("/register")
async def register(user: User):
    return user


# 定义请求体参数的模型（Pydantic模型，自动做参数校验）
class BookCreate(BaseModel):
    # 书名：必填，字符串
    book_name: str = Field(..., description="图书名称", example="《Python编程：从入门到实践》")
    # 作者：必填，字符串
    author: str = Field(..., description="作者", example="埃里克·马瑟斯")
    # 出版社：必填，字符串
    publisher: str = Field(..., description="出版社", example="人民邮电出版社")
    # 售价：必填，数值（支持整数/小数）
    price: float = Field(..., description="图书售价", example=89.0)


# 定义POST接口：新增图书
@app.post("/books", summary="新增图书", description="提交图书信息，完成新增")
def create_book(book_info: BookCreate):
    # 这里仅做示例：实际项目中会将book_info写入数据库
    return {
        "code": 200,
        "message": "新增图书成功",
        "data": {
            "book_name": book_info.book_name,
            "author": book_info.author,
            "publisher": book_info.publisher,
            "price": book_info.price
        }
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
