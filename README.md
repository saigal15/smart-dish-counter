# smart-dish-counter
Weight-based dish counting system for rental business

## Problem
Dish counting in event rental businesses is manual, slow and error-prone.

## Goal
Build a simple, low-cost system to count returned dishes using weight,
with a deployable and automated DevOps-oriented architecture.



# Liste de type de vaisselle
- Grande Assiette
- Petite Assiette
- Verre à eau
- Verre à vin
- Flute champagne
- Couvert complet (Cuillère à soupe, fourchette, couteau, cuillère à dessert)




# Solution

The system allows users to:

Select a dish type

Input total weight

Automatically calculate quantity

👉 Formula used:

quantity = total_weight / unit_weight
- 
## Architecture

The project uses a simple three-tier architecture:

- **Frontend**: Web interface for dish counting
- **Backend**: FastAPI REST API handling business logic and calcumlations
- **Database**: PostgreSQL for persistent storage ( stores dish types and return history)

All components are containerized using Docker and orchestrated with docker-compose.

## Tech Stack

Python (FastAPI)

PostgreSQL

SQLAlchemy

Docker / Docker Compose

Uvicorn

## Database Schema
dish_types
Field	Type
id	int
name	string
unit_weight	int

## returns
Field	Type
id	int
dish_type_id	int
total_weight	int
quantity	int
created_at	timestamp

## Getting Started
1. Start PostgreSQL
docker-compose up -d
2. Setup Backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3. Run API
uvicorn app.main:app --reload --port 8001
4. Access API Docs

👉 http://127.0.0.1:8001/docs

# Example API Request
{
  "dish_type_id": 1,
  "total_weight": 12000
}
# Example Response
{
  "dish_type": "Grande assiette",
  "unit_weight": 600,
  "total_weight": 12000,
  "quantity": 20
}
## Roadmap

 Database setup (PostgreSQL)

 Backend API (FastAPI)

 Calculation logic

 Input validation (Pydantic)

 Frontend UI

 Docker full stack

 CI/CD pipeline

## Future Improvements

Add dashboard & analytics

Multi-user support

Hardware integration (IoT)

SaaS deployment