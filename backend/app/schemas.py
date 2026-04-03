from pydantic import BaseModel
from datetime import datetime


class CalculateRequest(BaseModel):
    dish_type_id: int
    total_weight: int


class CalculateResponse(BaseModel):
    dish_type: str
    unit_weight: int
    total_weight: int
    quantity: int


class ReturnResponse(BaseModel):
    id: int
    dish_type: str
    total_weight: int
    quantity: int
    created_at: datetime   # ✅ correction ici

    class Config:
        from_attributes = True   # ✅ correction Pydantic v2