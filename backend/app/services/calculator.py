def calculate_quantity(unit_weight: int, total_weight: int) -> int:
    if unit_weight <= 0:
        raise ValueError("Unit weight must be greater than zero")
    return total_weight // unit_weight