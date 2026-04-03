from fastapi import FastAPI
from app.routers import returns

app = FastAPI(title="Smart Dish Counter API")

app.include_router(returns.router)