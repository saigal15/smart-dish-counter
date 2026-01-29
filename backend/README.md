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



