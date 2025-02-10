import pytest
from .connection import db_connection_handler
from sqlalchemy.engine import Engine


@pytest.mark.skip(reason="interação com o banco de dados")
def test_connect_to_db():
    assert db_connection_handler.get_engine() is None

    db_connection_handler.connect_to_db()
    db_engine = db_connection_handler.get_engine()

    assert db_engine is not None
    assert isinstance(db_engine, Engine)