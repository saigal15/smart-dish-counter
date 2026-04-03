from app.models import Return
from sqlalchemy.orm import Session

def create_return(db: Session, dish_type_id: int, total_weight: int, quantity: int) -> Return:
    new_return = Return(
        dish_type_id=dish_type_id,
        total_weight=total_weight,
        quantity=quantity
    )
    db.add(new_return)
    db.commit()
    db.refresh(new_return)
    return new_return

def get_all_returns(db: Session):
    return db.query(Return).all()