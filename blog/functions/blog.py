from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas

def get_all(db: Session):

    blogs = db.query(models.Blog).all()
    return blogs


def get_blog(id: int, db: Session):

    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'Blog with id {id} not found')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with id {id} not found'}
    return blog


def create(request: schemas.Blog, db: Session):

    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog


def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if blog.first():
        blog.delete(synchronize_session=False)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with {id} not found')

    db.commit()

    return f'Blog with id {id} deleted successfully'


def update(id: int, request: schemas.Blog, db: Session):
    
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if blog.first():
        blog.update({'title': request.title, 'body': request.body})
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with {id} not found')

    db.commit()
    return 'updated successfully'