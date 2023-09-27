from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException
from typing import List


from modules import User, Gender, Role


app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Dias",
        last_name='Muratbayev',
        # middle_name='Olegovich',
        gender=Gender.male,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="Josh",
        last_name='Forman',
        middle_name='yurievich',
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]


@app.get('/')
async def root():
    return {"Hello": "World"}


@app.get('/api/v1/users')
async def fetchall_user():
    return db


@app.post('/api/v1/users')
async def register_user(user: User):
    db.append(user)
    return {"id": user.id, "name": user.first_name}


@app.delete('/api/v1/users/{user_id}')
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f'User with id {user_id} not found'
    )
