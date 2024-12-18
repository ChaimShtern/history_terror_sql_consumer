from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.models import Base


class Attack(Base):
    __tablename__ = 'attacks'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)

    attack_type1 = Column(String)
    attack_type2 = Column(String)
    attack_type3 = Column(String)

    summary = Column(Text)
    additional_notes = Column(Text)
    source1 = Column(Text)
    source2 = Column(Text)
    source3 = Column(Text)

    target_type = Column(String)
    target_description = Column(Text)
    target_nationality = Column(String)

    location_id = Column(Integer, ForeignKey("locations.id"))
    location = relationship("Location", back_populates="attacks")

    group_id = Column(Integer, ForeignKey("groups.id"))
    group = relationship("Group", back_populates="attacks")

    weapons = relationship("Weapon", back_populates="attack")
    casualties = relationship("Casualty", back_populates="attack")
    property_damage = relationship("PropertyDamage", back_populates="attack")
    hostage_situation = relationship("HostageSituation", back_populates="attack")
