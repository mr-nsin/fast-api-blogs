from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str

@app.post('/blog')
def create(request: Blog):
    return 'creating'


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app="main:app", port=9000, reload=True )