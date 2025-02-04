from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {'data': {'name': 'Sarthak'}}


@app.get('/about')
def about():
    return {'data' : {'about': 'My name is nitin'}}

@app.get('/blog/{id}')
def show(id: int):
    print(type(id))
    return {'data': id}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': "unpublished"}

if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=9000, reload=True)