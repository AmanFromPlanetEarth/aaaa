from sqlalchemy import create_engine, String, Boolean
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column, Session


engine = create_engine('sqlite:///db.sqlite', echo=True)


new_session = Session(engine)

class Model(DeclarativeBase):
    pass

