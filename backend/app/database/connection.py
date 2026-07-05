from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:postgres@localhost:5433/rai_db"

engine = create_engine(DATABASE_URL)
