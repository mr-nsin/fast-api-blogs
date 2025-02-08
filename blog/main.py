from fastapi import FastAPI
import models
from database import engine
from routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(router=authentication.router)
app.include_router(router=blog.router)
app.include_router(router=user.router)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app="main:app", port=9000, reload=True )