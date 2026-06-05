import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

print("Database connection created.")

# Loading code will be added later

print("Database loading completed.")