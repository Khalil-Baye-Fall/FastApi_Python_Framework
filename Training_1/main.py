from fastapi import FastAPI
from schemas import Items

app = FastAPI()

fakeDatabase = {
    1:{"task 1": "First task"},
    2:{"task 2": "Second task"},
    3:{"task 3": "Third task"}
}

@app.get("/")
def getItem():
    return fakeDatabase

@app.get("/single_id/id")
def getSingleId(id:int):
    return fakeDatabase[id]

@app.post("/add_item")
def AddItem(task:Items):
    newId = len(fakeDatabase.keys()) + 1
    fakeDatabase[newId] = {f"task {newId}": task.item}
    return fakeDatabase

@app.put("/{id}")
def updateItem(id: int, item:Items):
    fakeDatabase[id]['task'] = item.task
    return fakeDatabase