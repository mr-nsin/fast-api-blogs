from pydantic import BaseModel
from typing import Optional, List

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True

class BlogUpdate(BaseModel):
    title: str
    body: str


class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator : ShowUser
    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str