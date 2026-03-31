from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class DishType(Base):
    __tablename__ = "dish_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    unit_weight = Column(Integer, nullable=False)


class Return(Base):
    __tablename__ = "returns"

    id = Column(Integer, primary_key=True, index=True)
    dish_type_id = Column(Integer, ForeignKey("dish_types.id"))
    total_weight = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)