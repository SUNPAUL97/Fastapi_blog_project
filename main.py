from fastapi import FastAPI
import sys, time
sys.path.append("C:/Users/MC MAGGIE/Downloads/FASTAPI/router")
from router import users,blog_get,blog_post,article, product, file
from templates import templates
from auth import authentication
from router.exceptions import StoryException
from DB import models
from DB.database import engine
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.include_router(templates.router)
app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(file.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
@app.get('/hello')

def index():
    return "Hello World!"
@app.exception_handler(StoryException)

def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={'details': exc.name}
    )
# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc),status_code=400)


models.Base.metadata.create_all(engine)
app.middleware("http")
async def add_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    response.headers['duration'] = str(duration)
    return response

origins = [
  'http://localhost:3000'
]

app.add_middleware(
  CORSMiddleware,
  allow_origins = origins,
  allow_credentials = True,
  allow_methods = ["*"],
  allow_headers = ['*']
)


app.mount("/files", StaticFiles(directory="files"), name="files")
app.mount("/templates/static", StaticFiles(directory="templates/static"), name="static")


