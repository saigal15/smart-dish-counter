# smart-dish-counter
Weight-based dish counting system for rental business

## Problem
Dish counting in event rental businesses is manual, slow and error-prone.

## Goal
Build a simple, low-cost system to count returned dishes using weight,
with a deployable and automated DevOps-oriented architecture.



#Liste de type de vaisselle
- Grande Assiette
- Petite Assiette
- Verre à eau
- Verre à vin
- Flute champagne
- Couvert complet (Cuillère à soupe, fourchette, couteau, cuillère à dessert)
- 
## Architecture

The project uses a simple three-tier architecture:

- **Frontend**: Web interface for dish counting
- **Backend**: FastAPI REST API handling business logic
- **Database**: PostgreSQL for persistent storage

All components are containerized using Docker and orchestrated with docker-compose.
