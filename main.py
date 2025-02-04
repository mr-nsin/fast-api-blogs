from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {'data': {'name': 'Sarthak'}}


@app.get('/about')
def about():
    return {'data' : {'about': 'My name is nitin'}}
    
if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=9000, reload=True)