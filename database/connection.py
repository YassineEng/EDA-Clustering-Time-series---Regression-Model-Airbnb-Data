import os
import urllib.parse
import pyodbc
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_pyodbc_connection():
    """Establish a pyodbc connection using environment variables."""
    server_name = os.getenv("SERVER_NAME")
    mdf_file = os.getenv("MDF_FILE")
    db_name = os.getenv("DB_NAME")
    timeout = os.getenv("TIMEOUT", "30")

    if not all([server_name, mdf_file, db_name]):
        raise ValueError("❌ Missing required database configuration in .env file")

    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server_name};"
        f"Trusted_Connection=yes;"
        f"AttachDbFilename={mdf_file};"
        f"DATABASE={db_name};"
        f"Connection Timeout={timeout};"
    )

    try:
        cnxn = pyodbc.connect(conn_str)
        print("✅ Successfully connected to SQL Server via pyodbc.")
        return cnxn
    except pyodbc.Error as ex:
        print("❌ Error connecting to the database:", ex)
        raise

def get_sqlalchemy_engine():
    """Create a SQLAlchemy engine for high-level database access."""
    cnxn = get_pyodbc_connection()
    params = urllib.parse.quote_plus(cnxn.getinfo(pyodbc.SQL_DRIVER_NAME))
    params = urllib.parse.quote_plus(cnxn.getinfo(pyodbc.SQL_DRIVER_ODBC_VER))

    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={os.getenv('SERVER_NAME')};"
        f"Trusted_Connection=yes;"
        f"AttachDbFilename={os.getenv('MDF_FILE')};"
        f"DATABASE={os.getenv('DB_NAME')};"
    )
    encoded_params = urllib.parse.quote_plus(conn_str)
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={encoded_params}")
    print("✅ SQLAlchemy engine created successfully.")
    return engine
