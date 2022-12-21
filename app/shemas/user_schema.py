from pydantic import BaseModel
from datetime import datetime 

class User(BaseModel):
    name: str
    age: int
    birth_date: datetime

    class Config:
        orm_mode = True

class ShowUser(User):
    id: int