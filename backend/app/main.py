from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import DishType, Return

app = FastAPI()


@app.post("/calculate")
def calculate(dish_type_id: int, total_weight: int):
    db: Session = SessionLocal()

    # 1. récupérer type de vaisselle
    dish = db.query(DishType).filter(DishType.id == dish_type_id).first()

    if not dish:
        raise HTTPException(status_code=404, detail="Dish type not found")

    # 2. calcul
    quantity = total_weight // dish.unit_weight

    # 3. sauvegarde
    new_return = Return(
        dish_type_id=dish_type_id,
        total_weight=total_weight,
        quantity=quantity
    )

    db.add(new_return)
    db.commit()

    # 4. réponse
    return {
        "dish_type": dish.name,
        "unit_weight": dish.unit_weight,
        "total_weight": total_weight,
        "quantity": quantity
    }