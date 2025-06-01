import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus
# Load environment variables from a .env file (optional, useful for local dev)
load_dotenv()

# Read DB credentials from environment variables
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = quote_plus(os.getenv("DB_PASSWORD"))


def db_conn():
    connection = None
    try:
        connection = create_engine(
            f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
        )

        return connection

    except Exception as e:

        return None

    finally:
        if connection:
            connection.dispose()
