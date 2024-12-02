import os
from dotenv import load_dotenv

load_dotenv("../env.env")

# Чтение и установка env
# DB_CONFIG = {
#     "dbname": os.getenv("DB_NAME"),
#     "user": os.getenv("DB_USER"),
#     "password": os.getenv("DB_PASSWORD"),
#     "host": os.getenv("DB_HOST"),
#     "port": os.getenv("DB_PORT"),
# }

DB_CONFIG = {
    "dbname": "course",
    "user": "postgres",
    "password": "gangball08",
    "host": "localhost",
    "port": "5432",
}

# Pool settings
POOL_MIN_CONN = int(os.getenv("POOL_MIN_CONN", 1))
POOL_MAX_CONN = int(os.getenv("POOL_MAX_CONN", 10))