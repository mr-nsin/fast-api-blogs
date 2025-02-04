from fastapi import FastAPI
from typing import Optional
app = FastAPI()


@app.get("/")
def index():
    return {'data': {'name': 'Sarthak'}}

@app.get('/blog')
def index(limit, published):
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



if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=9000, reload=True)