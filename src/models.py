#Import needed components from the module
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()



class Category(Base):
    __tablename__="categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    notes = relationship("Note", back_populates="category")
    
class Note(Base):
    __tablename__="notes"
    id = Column(Integer, primary_key=True)
    title = Column(String(30))
    content = Column(Text)

    category_id=Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category",back_populates="notes")


