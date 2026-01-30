
from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5544/oncalldb"
)

def run_sql(query: str):
    with engine.connect() as conn:
        result = conn.execute(text(query))
        return result.fetchall()


