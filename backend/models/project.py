from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Project(Base):

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)

    nombre = Column(String)

    artista = Column(String)

    genero = Column(String)

    descripcion = Column(String)