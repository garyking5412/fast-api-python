from fastapi import FastAPI, HTTPException, Depends, Query, Path
from typing import Annotated, List
from sqlalchemy.orm import Session

from models.models import *
from database.database import SessionLocal
from dto.dto import CategoryRequest, CategoryResponse, ProductResponse

app = FastAPI()
# models.models.Base.metadata.create_all(bind=engine)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    except Exception as exception:
        raise HTTPException(status_code=500,detail = f"Failed to establish Database connection >>> Error: {exception}")
    finally:
        db.close()

db_dependency = Annotated[Session,Query(description="Search query string"), Depends(get_db)]

def test_exception(exception):
    raise HTTPException(status_code=500, detail=f"Failed to establish Database connection >>> Error: {exception}")

@app.post("/category/", response_model=CategoryResponse)
async def create_category(request:CategoryRequest, db:db_dependency):
    db_category = Category(name = request.name, detail = request.detail)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    for product in request.products:
        db_product = Product(name = product.name, detail = product.detail, price = product.price, image = product.image, cateid = db_category.id)
        db.add(db_product)
        db.commit()
    return db_category

@app.get("/category/all",response_model=List[CategoryResponse])
def get_all_category(db:db_dependency):
    db_categories = db.query(Category).all()
    return db_categories

@app.get("/product/all",response_model=List[ProductResponse])
def get_all_products(db:db_dependency):
    db_products = db.query(Product).all()
    return db_products

@app.delete("/category/all")
def delete_all_products(db:db_dependency):
    db.query(Category).delete()
    db.commit()
    return HTTPException(status_code=200, detail="Delete all categories succeeded!")