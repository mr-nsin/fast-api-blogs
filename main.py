from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    author: str
    title: str
    body: str
    published: Optional[str]

@app.get("/")
def index():
    return {'data': {'name': 'Sarthak'}}

@app.get('/blog')
def index(limit: int = 10, published: bool = False, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}
    
@app.get('/about')
def about():
    return {'data' : {'about': 'My name is nitin'}}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': "unpublished blogs"}

@app.get('/blog/{id}')
def show(id: int):
    print(type(id))
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {'data': {'1', '2'}}


@app.post('/blog')
def create_blog(request: Blog):
    return request

if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=9000, reload=True)