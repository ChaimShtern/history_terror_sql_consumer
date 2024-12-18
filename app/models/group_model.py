from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.models import Base


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String)
    uncertain = Column(Boolean)
    num_perpetrators = Column(Integer)

    attacks = relationship("Attack", back_populates="group")
