from pydantic import BaseModel

class TaskCreateSchemas(BaseModel):
    title:str
    descrription:str
    