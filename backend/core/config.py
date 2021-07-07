from starlette.config import Config
from starlette.datastructures import Secret

config = Config("backend/.env")

PROJECT_NAME = "catcord"
VERSION = "1.0.0"

POSTGRES_USER = config("POSTGRES_USER", cast=str)
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret)
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="db")
POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
POSTGRES_DB = config("POSTGRES_DB", cast=str)

DATABASE_URL = config(
    "DATABASE_URL",
    cast=str,
    default=f"postgresql://"
    f"{POSTGRES_USER}:"
    f"{POSTGRES_PASSWORD}@"
    f"{POSTGRES_SERVER}:"
    f"{POSTGRES_PORT}/"
    f"{POSTGRES_DB}",
)
