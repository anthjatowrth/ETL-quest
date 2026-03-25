import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

username = "root"
password = "futu.Re503"
host = "localhost"
port = 3306
database = "my_dbt_db"

DATABASE_URI = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(DATABASE_URI)

if not database_exists(engine.url):
    create_database(engine.url)

liste_tables = ["customers", "items", "orders", "products", "stores", "supplies"]

for table in liste_tables:
    csv_url = f"https://github.com/dbt-labs/jaffle-shop-data/raw/refs/heads/main/jaffle-data/raw_{table}.csv"
    df = pd.read_csv(csv_url)
    with engine.begin() as conn:  # ← seul changement
        df.to_sql(f"raw_{table}", conn, if_exists="replace", index=False)
        print(f"✅ raw_{table} chargée ({len(df)} lignes)")