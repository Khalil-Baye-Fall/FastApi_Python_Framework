from pyexpat import model
from random import seed
from fastapi import FastAPI, Body, Depends
from schemas import Items

import models
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session


Base.metadata.create_all(engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

app = FastAPI()

fakeDatabase = {
    1:{"task": "First task"},
    2:{"task": "Second task"},
    3:{"task": "Third task"}
}

@app.get("/")
def getItem(session: Session= Depends(get_session)):
    items = session.query(models.Items).all()
    return items

@app.get("/single_id/id")
def getSingleId(id:int, session: Session= Depends(get_session)):
    item = session.query(models.Items).get(id)
    
    return item

@app.post("/add_item")
def AddItem(item:Items, session: Session= Depends(get_session)):
    item= models.Items(task=item.task)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@app.put("/{id}")
def updateItem(id: int, item:Items, session: Session= Depends(get_session)):
    itemObject= session.query(models.Items).get(id)
    itemObject.task = item.task
    session.commit()
    return itemObject

@app.delete("/delete/{id}", )
def delete_item(id: int, session: Session= Depends(get_session)):
    itemObject= session.query(models.Items).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    return "item was deleted successully."    