from fastapi import APIRouter, HTTPException
from app.database import SessionLocal
from app.models import DishType
from app.schemas import CalculateRequest, CalculateResponse, ReturnResponse
from app.services.calculator import calculate_quantity
from app.crud.returns import create_return, get_all_returns

router = APIRouter()

@router.post("/calculate", response_model=CalculateResponse)
def calculate(request: CalculateRequest):
    db = SessionLocal()

    dish = db.query(DishType).filter(DishType.id == request.dish_type_id).first()

    if not dish:
        raise HTTPException(status_code=404, detail="Dish type not found")

    quantity = calculate_quantity(dish.unit_weight, request.total_weight)

    create_return(db, request.dish_type_id, request.total_weight, quantity)

    return {
        "dish_type": dish.name,
        "unit_weight": dish.unit_weight,
        "total_weight": request.total_weight,
        "quantity": quantity
    }


@router.get("/returns", response_model=list[ReturnResponse])
def get_returns():
    db = SessionLocal()
    results = get_all_returns(db)

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
