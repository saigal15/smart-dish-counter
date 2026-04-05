# 🍽️ Smart Dish Counter

Smart Dish Counter is a lightweight web application designed to help dish rental businesses automatically count returned items using weight-based calculations.

## 🎯 Problem
Manual counting of returned dishes is:
- Time-consuming
- Error-prone
- Stressful during large events

## 💡 Solution
A simple web application that:
- Calculates quantities based on weight
- Compares returned items with rented quantities
- Highlights missing or broken items

## 🧱 Tech Stack
- Backend: Python / FastAPI
- Frontend: HTML / JavaScript (future)
- Database: PostgreSQL (planned)
- DevOps: Docker, Docker Compose, GitHub Actions
- Infra: Ubuntu Server (VM), SSH, Nginx (planned)

## 🗂️ Project Structure
```text
smart-dish-counter/
├── backend/
├── frontend/
├── infra/
├── .github/
└── README.md

## 🚀 Backend Setup
- cd backend
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- uvicorn app.main:app --reload

## Health Check

GET /health - {"status":"ok"}

## DevOps Focus

This project emphasizes:

Real business problem solving

Automation

Clean architecture

Production-oriented thinking

## Setup Python Virtual Environment

### Tasks
- Create Python virtual environment
- Activate environment
- Install FastAPI and Uvicorn
- Generate requirements.txt

### Outcome
Isolated Python environment ready for backend development.


## Lancer PostgreSQL avec Docker
docker-compose up -d

### Vérifier que le conteneur tourne :

docker ps
Base de données

Connexion :

docker exec -it smart-dish-db psql -U user -d smartdish

### Tables existantes :

dish_types
returns
### Lancer l’API
uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
## Accès API

### Swagger UI :

http://127.0.0.1:8001/docs
Endpoints
##POST /calculate

Calcule le nombre de plats à partir du poids total.

Exemple request :
{
  "dish_type_id": 1,
  "total_weight": 12000
}
Exemple response :
{
  "dish_type": "Grande assiette",
  "unit_weight": 600,
  "total_weight": 12000,
  "quantity": 20
}
## GET /returns

Retourne tous les calculs enregistrés.

Exemple :
[
  {
    "id": 1,
    "dish_type": "Grande assiette",
    "total_weight": 12000,
    "quantity": 20,
    "created_at": "2026-03-30T23:39:52.350127"
  }
]
## Structure du projet
app/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud/
│   └── returns.py
├── routers/
│   ├── calculate.py
│   └── returns.py
└── services/
    └── calculator.py



### Build Docker image

docker build -t smart-dish-backend .

### Run container

docker run -p 8001:8001 smart-dish-backend

### Access API

Swagger UI:
http://localhost:8001/docs

### Available endpoints

- POST /calculate
- GET /returns




