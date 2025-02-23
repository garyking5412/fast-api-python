from typing import Annotated

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models.models
from database.database import SessionLocal, engine
from dto.dto import CategoryRequest

app = FastAPI()
# models.models.Base.metadata.create_all(bind=engine)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]

@app.post("/category/")
async def create_category(request:CategoryRequest, db:db_dependency):
    db_category = models.models.Category(name = request.name, detail = request.detail)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    for product in request.products:
        db_product = models.models.Product(name = product.name, detail = product.detail, price = product.price, image = product.image, cateid = db_category.id)
        db.add(db_product)
        db.commit()
    return db_category
