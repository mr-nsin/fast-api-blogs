from fastapi import FastAPI
from schemas import Blog

app = FastAPI()


@app.post('/blog')
def create(request: Blog):
    return request


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app="main:app", port=9000, reload=True )