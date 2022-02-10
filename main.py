"""
FastAPI - A python framework | Full Course

"""

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # specify a limit and published as query parameters
    # default limit amount is 10 and default published is true, sort is optional
    if published:
        return {'data': f'{limit} published blogs from db'}
    else:
        return {'data': f'{limit} unpublished blogs from db'}


@app.get('/blog/unpublished')
def get_unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int):

    return {'data': {'1', '2'}}


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'blog created with title {request.title}'}


if __name__ == '__main__':
    uvicorn.run(app, port=5000)