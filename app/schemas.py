from pydantic import BaseModel

class TaskCreateSchema(BaseModel):
    title:str
    description:str
class TaskUpdateShemas(TaskCreateSchema):
    status:bool