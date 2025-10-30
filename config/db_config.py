# config/db_config.py
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

DB_CONFIG = {
    "server": os.getenv("DB_SERVER"),
    "database": os.getenv("DB_NAME"),
    "mdf_path": os.getenv("DB_MDF_PATH"),
    "driver": os.getenv("ODBC_DRIVER", "ODBC Driver 17 for SQL Server"),
    "trusted_connection": os.getenv("DB_TRUSTED_CONNECTION", "yes")
}
