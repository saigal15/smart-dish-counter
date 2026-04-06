from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de la base PostgreSQL
DATABASE_URL = "postgresql://user:password@db:5432/smartdish"

# Créer l'engine SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)  # echo=True affiche les requêtes SQL dans la console

# Créer une session locale
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base déclarative pour les modèles
Base = declarative_base()

# Optionnel : fonction pour obtenir une session DB via Depends
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()