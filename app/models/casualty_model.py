from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.models import Base


class Casualty(Base):
    __tablename__ = 'casualties'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    killed = Column(Integer)
    wounded = Column(Integer)

    attack_id = Column(Integer, ForeignKey("attacks.id"))
    attack = relationship("Attack", back_populates="casualties")
