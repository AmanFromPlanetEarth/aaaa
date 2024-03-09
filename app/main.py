from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI() #экземпляр
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')


@app.get('/') #декоратор, который обрабатывает get запросы по маршруту 127.0.0.1
def index (request:Request):
    return templates.TemplateResponse(request=request,name='index.html')

#ls команда показывающая в консоли папки и файлы
#cd app перейти в директорию app
#uvicorn main:app --reload
@app.get('/about/')
def about(request:Request):
    return templates.TemplateResponse(request=request,name='about.html')



@app.get('/login/')
def login(request:Request):
    data = {
        "first_name":"Aleksandr",
        "last_name":"Kovalev"
    }
    return data