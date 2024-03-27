from sqlalchemy import create_engine, String, Boolean
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, Session
from database import Model

class TaskModel(Model):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] 
    description: Mapped[str] 
    done: Mapped[bool] = mapped_column(Boolean, default=False)