import os

"""
DEVEL environment is understood as running a local instance of the app.

TESTING environment on the other hand is understood as running the unit tests
for the app.
"""
DEVEL = True
TESTING = bool(os.environ.get("TESTING"))

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Instead of editing this file to specify a host, you can just edit your /etc/hosts.
SQL_HOST = "db"
SQL_PORT = 3306
SQL_USERNAME = "root"
SQL_PASSWORD = ""
SQL_ENGINE = "mysql"
SQL_DB_NAME = "app"
SQL_TEST_DB_NAME = "%s_test" % SQL_DB_NAME
SQLALCHEMY_DATABASE_URI = '%s://%s:%s@%s:%d/%s' % (SQL_ENGINE, SQL_USERNAME,
  SQL_PASSWORD, SQL_HOST, SQL_PORT, SQL_DB_NAME)
SQLALCHEMY_TEST_DATABASE_URI = '%s://%s:%s@%s_test:%d/%s' % (SQL_ENGINE, SQL_USERNAME,
  SQL_PASSWORD, SQL_HOST, SQL_PORT, SQL_TEST_DB_NAME)
SQLALCHEMY_ECHO = DEVEL
DATABASE_CONNECT_OPTIONS = {"user":"root"}

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = not TESTING
WTF_CSRF_ENABLED = CSRF_ENABLED

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

APP_HOST="0.0.0.0"
APP_PORT=8080
