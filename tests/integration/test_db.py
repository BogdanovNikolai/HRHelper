"""
Пример интеграционного теста для PostgreSQL (pytest + testcontainers)
"""
from testcontainers.postgres import PostgresContainer
from sqlalchemy import create_engine

def test_db_connection():
    with PostgresContainer("postgres:15") as pg:
        engine = create_engine(pg.get_connection_url())
        conn = engine.connect()
        assert conn.closed is False
        conn.close() 