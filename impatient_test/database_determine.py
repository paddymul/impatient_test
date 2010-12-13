
import os

def test_database_engine():
    env_mysql = os.environ.get("PPY_MYSQL", False)
    if env_mysql:
        return "mysql"
    return "sqlite3"

def test_database_name():
    env_mysql_db_name = os.environ.get("PPY_MYSQL_NAME", False)
    if env_mysql_db_name:
        return env_mysql_db_name
    return ":memory:"

