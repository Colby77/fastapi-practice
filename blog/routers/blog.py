from http.client import HTTPException
from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session

from .. import schemas, database, oauth2
from ..functions import blog


router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.
                get_current_user)):

    return blog.get_all(db)
    # return current_user


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = 
                Depends(oauth2.get_current_user)):

    return blog.create(request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def get_blog_by_id(id: int, db: Session = Depends(get_db), current_user: schemas.User = 
                    Depends(oauth2.get_current_user)):

    return blog.get_blog(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = 
                Depends(oauth2.get_current_user)):
    
    return blog.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db), current_user: schemas.User = 
                Depends(oauth2.get_current_user)):

    return blog.destroy(id, db)