#Import needed components from the module
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()



# Our models. Remove the demo "Note" and add your own

class Note(Base):
    __tablename__="notes"
    id = Column(Integer, primary_key=True)
    title = Column(String(30))
    content = Column(Text)



