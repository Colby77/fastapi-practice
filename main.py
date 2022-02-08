"""
FastAPI - A python framework | Full Course
https://www.youtube.com/watch?v=7t2alSnE2-I


"""

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': 'Beevis'}}


@app.get('/about')
def about():
    return {'data': 'about page'}