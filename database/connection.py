import os
import urllib.parse
import pyodbc
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from the .env file to configure the database connection.
load_dotenv()

def get_pyodbc_connection():
    """
    Establishes a pyodbc connection to a SQL Server database using environment variables.
    
    This function reads database configuration from a .env file, including the server name,
    MDF file path, database name, and connection timeout. It constructs a connection string
    for a trusted connection and returns a pyodbc connection object.

    Returns:
        pyodbc.Connection: A pyodbc connection object to the SQL Server database.

    Raises:
        ValueError: If any of the required environment variables are not set.
        pyodbc.Error: If the database connection fails.
    """
    # Retrieve database connection details from environment variables.
    server_name = os.getenv("SERVER_NAME")
    mdf_file = os.getenv("MDF_FILE")
    db_name = os.getenv("DB_NAME")
    timeout = os.getenv("TIMEOUT", "30")

    # Validate that all required environment variables are present.
    if not all([server_name, mdf_file, db_name]):
        raise ValueError("❌ Missing required database configuration in .env file")

    # Construct the connection string for a trusted connection.
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server_name};"
        f"Trusted_Connection=yes;"
        f"AttachDbFilename={mdf_file};"
        f"DATABASE={db_name};"
        f"Connection Timeout={timeout};"
    )

    try:
        # Establish the pyodbc connection.
        cnxn = pyodbc.connect(conn_str)
        print("✅ Successfully connected to SQL Server via pyodbc.")
        return cnxn
    except pyodbc.Error as ex:
        # Raise an exception if the connection fails.
        print("❌ Error connecting to the database:", ex)
        raise

def get_sqlalchemy_engine():
    """
    Creates a SQLAlchemy engine for high-level database access.

    This function reuses the pyodbc connection string from the environment variables
    to create a SQLAlchemy engine. The engine provides a consistent interface for
    database operations and connection pooling.

    Returns:
        sqlalchemy.engine.Engine: A SQLAlchemy engine instance.
    """
    # Construct the connection string from environment variables.
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={os.getenv('SERVER_NAME')};"
        f"Trusted_Connection=yes;"
        f"AttachDbFilename={os.getenv('MDF_FILE')};"
        f"DATABASE={os.getenv('DB_NAME')};"
    )
    
    # URL-encode the connection string to handle special characters.
    encoded_params = urllib.parse.quote_plus(conn_str)
    
    # Create the SQLAlchemy engine with the encoded connection string.
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={encoded_params}")
    
    print("✅ SQLAlchemy engine created successfully.")
    return engine
