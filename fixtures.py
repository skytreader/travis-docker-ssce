from main.models import get_or_create
from config import SQLALCHEMY_DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def insert_fixtures(engine, session):
    """
    Add your default data here. Use `get_or_create` when applicable.

    :param engine
    :param session
    """
    pass

if __name__ == "__main__":
    engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
    session = sessionmaker(bind=engine)()

    insert_fixtures(engine, session)
