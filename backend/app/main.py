from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import DishType, Return
from app.schemas import CalculateRequest, CalculateResponse, ReturnResponse

app = FastAPI()

@app.post("/calculate", response_model=CalculateResponse)
def calculate(request: CalculateRequest):
    db = SessionLocal()

    dish = db.query(DishType).filter(DishType.id == request.dish_type_id).first()

    if not dish:
        raise HTTPException(status_code=404, detail="Dish type not found")

    quantity = request.total_weight // dish.unit_weight

    new_return = Return(
        dish_type_id=request.dish_type_id,
        total_weight=request.total_weight,
        quantity=quantity
    )

    db.add(new_return)
    db.commit()

    return {
        "dish_type": dish.name,
        "unit_weight": dish.unit_weight,
        "total_weight": request.total_weight,
        "quantity": quantity
    }

@app.get("/returns", response_model=list[ReturnResponse])
def get_returns():
    db = SessionLocal()

    results = db.query(Return).all()

    response = []

    for r in results:
        dish = db.query(DishType).filter(DishType.id == r.dish_type_id).first()
        dish_name = dish.name if dish else "Unknown"

        response.append({
            "id": r.id,
            "dish_type": dish_name,
            "total_weight": r.total_weight,
            "quantity": r.quantity,
            "created_at": r.created_at
        })

    return response