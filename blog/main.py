from fastapi import FastAPI
from .schemas import Blog
# from . import schemas would also work - schemas.Blog

app = FastAPI()


@app.post('/blog')
def create_blog(request: Blog):
    return request

