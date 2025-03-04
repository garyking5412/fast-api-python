from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database.database import Base


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    detail = Column(String, index=True)
    products = relationship("Product", backref="category", cascade='all, delete-orphan')

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    detail = Column(String, index=True)
    image = Column(String, index=True)
    price = Column(Integer)
    createddate = Column(DateTime, default=datetime.now())
    cateid = Column(Integer, ForeignKey("category.id", ondelete='CASCADE'))
    # category = relationship("Category", back_populates="products")
