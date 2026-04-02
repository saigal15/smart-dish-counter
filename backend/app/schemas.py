from pydantic import BaseModel, Field
from datetime import datetime

class CalculateRequest(BaseModel):
    dish_type_id: int = Field(..., example=1)
    total_weight: int = Field(..., gt=0, example=12000)


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
    created_at: datetime