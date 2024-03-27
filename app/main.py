import select
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json
from fastapi.responses import HTMLResponse
import uvicorn
from database import Model, engine, new_session
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import select
from pydantic import BaseModel
from database import Model, engine
from routers import tasks_router
from models import TaskModel

URLS = [
    {"task_post": "127.0.0.1:8000/tasks/"}
]

app = FastAPI() #экземпляр
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

app.include_router(tasks_router)



if __name__ == '__main__':
    TaskModel.metadata.create_all(engine)
    print('Start server')
    uvicorn.run('main:app', port=8000, reload=True)
    print('server stopped')


"""@app.post('/task_list/')
def create_task(request:Request,title:str = Form(...), description:str = Form(...)):
    print(title, description)
    tasks = read_file(DATABASE, 'r')
    return templates.TemplateResponse(request=request, name='task_list.html', context=tasks)
#ls команда показывающая в консоли папки и файлы
#cd app перейти в директорию app
#uvicorn main:app --reload
@app.get('/task_list/')
def list_task(request:Request):
    tasks = read_file(DATABASE, 'r')
    return templates.TemplateResponse(request=request, name='task_list.html', context=tasks)

@app.get('/user_list/')
def list_task(request:Request):
    users = read_file(DATABASE, 'r')
    return templates.TemplateResponse(request=request, name='user_list.html', context=users)"""