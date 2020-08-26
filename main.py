from fastapi import FastAPI
from uuid import UUID
from models import TagModel, TaskModel


app = FastAPI(debug=True)

# Start database testing..
database = []


# Root Router
@app.get("/")
def root():
    return {'message': "Welcome to To-Do"}


# Routes Tag
@app.get("/api/v1/tags")
async def get_all_tags():
    print(database)
    return database


@app.post("/api/v1/tag/")
async def create_tag(tag: TagModel):
    database.append(tag)
    return tag


@app.put('/api/v1/tag/{id_tag}')
async def update_tag(id_tag: int):
    for tag in database:
        if(tag.id == id_tag):
            return tag
    return {"status_code": 404, "message": "Not found id tag."}


@app.delete('/api/v1/tag/{id_tag}')
async def delete_tag(id_tag: int):
    for tag in database:
        if(tag.id == id_tag):
            database.remove(tag)
            return tag
    return {"status_code": 404, "message": "Not found id tag."}


# Routes Task
@app.get("/api/v1/task")
async def get_all_task():
    print(database)
    return database


@app.post("/api/v1/task/")
async def create_task(task: TaskModel):
    database.append(task)
    return task


@app.put('/api/v1/task/{id_task}')
async def update_task(id_task: int):
    for task in database:
        if(task.id == id_task):
            return task
    return {"status_code": 404, "message": "Not found id task."}


@app.delete('/api/v1/task/{id_task}')
async def delete_task(id_task: int):
    for task in database:
        if(task.id == id_task):
            database.remove(task)
            return task
    return {"status_code": 404, "message": "Not found id task."}