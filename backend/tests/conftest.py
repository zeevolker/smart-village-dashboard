import pytest

from app.database.database import SessionLocal


@pytest.fixture
def db():
    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()