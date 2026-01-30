

from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5544/oncalldb"
)

from sqlalchemy import create_engine, text

def run_sql(query: str):
    with engine.connect() as conn:
        result = conn.execute(text(query))
        return result.fetchall()
