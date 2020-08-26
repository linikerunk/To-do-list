import datetime
from typing import Optional
from pydantic import BaseModel, validator


# Create your Models here.

class TagModel(BaseModel):
    id: int
    name: str
    created: datetime = datetime.time


class TaskModel(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    tag: Optional[TagModel] = None
    created: datetime = datetime.time
    completed: bool = False
