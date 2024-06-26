from fastapi import APIRouter, Request
from sqlalchemy.orm import Session
from database import engine
from sqlalchemy import select, insert, update, delete
from models import TaskModel
from schemas import TaskCreateSchema, TaskUpdateShemas


tasks_router = APIRouter(prefix="/api/v1/tasks")

@tasks_router.get(path='/list/') #декоратор который указывает что ф-ция определенная ниже будет обрабатывать запрос по такому пути как /list/, полный путь /api/v1/tasks/list/
def list_task_point(request:Request): #функция которая принимает параметр request типа Request, который содержит в себе информацию о запросе пользователя
    """file = open('data.txt')
    file.write()"""
    session = Session(engine) #создает экземпляр класса сессиии для работы с базой данных. Используется для подключения к БД
    stmt = select(TaskModel) #формирует sql запрос для выборки всех записей из таблицы сопоставленной с моделью TaskModel

    request_db = session.execute(stmt) #запрос выполняется с помощью созданной сессии, в результате мы получаем объект, который содержит результат запроса
    tasks:list = request_db.scalars().all()#полученный оъект с результатом преобразуем в список значений при помощи метода scalars() и из него извлекаются все значения с помощью метода all()
    session.close()# сессия закрывается для освобождения ресурсов связанных с БД

    if len(tasks) == 0:
        return {"Message" : "У вас нет задач"}
    else:
        return{"message":tasks}#возвращает словарь который преобразуется в json который будет возвращен клиенту в ответ на запрос
    

@tasks_router.post(path='/create/')
def create_task_point(request:Request, task: TaskCreateSchema):
    new_task = TaskModel(
        title = task.title,
        description = task.description
    )
    session = Session(engine)
    stmt = insert(TaskModel).values(title = task.title,
                                    description = task.description)
    session.execute(stmt)
    session.commit()
    session.close()
    return task

@tasks_router.put(path='/update/')
def update_task_point(request:Request,task_id:int, new_task:TaskCreateSchema):
    session = Session(engine)
    stmt = select(TaskModel).where(TaskModel.id == task_id)
    task = session.execute(stmt).scalar()
    task.title = new_task.title
    task.description = new_task.description
    task.status = new_task.status
    session.merge(task)
    session.commit()
    session.close()
    return new_task

@tasks_router.delete(path='/delete/')
def delete_task_point(request:Request,task_id:int):
    session = Session(engine)
    stmt = delete(TaskModel).where(TaskModel.id == task_id)
    task = session.execute(stmt)
    session.commit()
    session.close()
    return "Task delete"
