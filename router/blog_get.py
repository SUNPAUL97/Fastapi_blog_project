from fastapi import APIRouter, status, Response, Depends
from enum import Enum 
from typing import Optional
from router.blog_post import required_functionality

router = APIRouter(
    prefix = '/blog',
    tags = ['blog']
)

# using json format
@router.get('/json')
 
def home():
    return {"mesaage": "Welcome to FastAPI lesson"}

@router.get(
    '/all',
    
    summary = 'Get all blogs',
    description = 'This endpoint retrieves all blogs with pagination support',
         
         )
def get_blogs(page = 1, page_size: Optional[int] = None, req_params: dict = Depends(required_functionality)):
    return {'message': f'All {page_size} blogs on page{page}', 'req': req_params}
@router.get('/{id}/comments/{comment_id}', tags = ['comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = home,req_params: dict = Depends(required_functionality)):
    """
    Simulates retrieving a comment for a blog post.
    - **id**: The ID of the blog post.
    - **comment_id**: The ID of the comment.    
    - **valid**: Indicates if the comment is valid.
    - **username**: Optional username of the commenter.
    - Returns a message with the blog ID, comment ID, validity, and username.
    """
    return {'message': f'blog_id {id},comment_id {comment_id}, valid {valid}, username {username}'}
# Predefine value
class BlogType(str, Enum):
    short = 'short'
    story= 'story'
    howto = 'howto'
    
    
@router.get('/type/{type}')
def get_blog_type(type: BlogType,req_params: dict = Depends(required_functionality)):
    return {'message': f' Blog type {type}'}

#Path parameter
@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response,req_params: dict = Depends(required_functionality)):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id}'}