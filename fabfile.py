from config import (
  DEVEL, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TEST_DATABASE_URI, TESTING
)
from fabric.api import local
from fixtures import insert_fixtures
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""
Update this file as you add database tables.
"""

def __env_safeguard(fab_method):
    """
    This is not a fabric method per se. Useless to call this.
    """
    def check(*args, **kwargs):
        if DEVEL or TESTING:
            fab_method(*args, **kwargs)
        else:
            print "Prevented by env_safeguard"

    return check

@__env_safeguard
def reset_db_data():
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    session = sessionmaker(bind=engine)()
    engine.execute("SET FOREIGN_KEY_CHECKS = 0;")
    engine.execute("TRUNCATE alembic_version;")
    engine.execute("TRUNCATE users;")
    engine.execute("SET FOREIGN_KEY_CHECKS = 1;")
    session.commit()

    insert_fixtures(engine, session)

@__env_safeguard
def destroy_db_tables():
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    session = sessionmaker(bind=engine)()
    engine.execute("SET FOREIGN_KEY_CHECKS = 0;")
    engine.execute("DROP TABLE IF EXISTS alembic_version;")
    engine.execute("DROP TABLE IF EXISTS users;")
    engine.execute("SET FOREIGN_KEY_CHECKS = 1;")
    session.commit()

def manual_test_cleanup():
    engine = create_engine(SQLALCHEMY_TEST_DATABASE_URI)
    session = sessionmaker(bind=engine)()
    engine.execute("SET FOREIGN_KEY_CHECKS = 0;")
    engine.execute("DELETE FROM alembic_version;")
    engine.execute("DELETE FROM users;")
    engine.execute("SET FOREIGN_KEY_CHECKS = 1;")
    session.commit()

def dbdump():
    local("mysqldump -u root app > app.sql")

@__env_safeguard
def destroy_database(is_test=False):
    if is_test:
        local('mysql -u root -e "DROP DATABASE app_test"')
    else:
        local('mysql -u root -e "DROP DATABASE app"')

def create_database(is_test=False):
    if is_test: 
        local('mysql -u root -e "CREATE DATABASE app_test DEFAULT CHARACTER SET = utf8"')
    else:
        local('mysql -u root -e "CREATE DATABASE app DEFAULT CHARACTER SET = utf8"')
