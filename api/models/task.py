from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

from api.database import Base

class Task(Base):
    __tablename__ = "tasks"

    #Column(カラムの型,カラムの設定)
    id = Column(Integer,primary_key=True)
    title = Column(String(1024))

    done = relationship("Done",back_populates="task",cascade="delete")


class Done(Base):
    __tablename__ = "dones"

    id = Column(Integer,ForeignKey("tasks.id"),primary_key=True)

    task = relationship("Task",back_populates="done")
