from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel, ValidationError
from enum import Enum


class Gender(str, Enum):
    male = 'male'
    female = 'female'


class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = 'student'


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str] = ''
    gender: Gender
    roles: List[Role]


# try:
#     User()
# except ValidationError as exc:
#     print(repr(exc.errors()[0]['type']))
#     # > 'missing'
