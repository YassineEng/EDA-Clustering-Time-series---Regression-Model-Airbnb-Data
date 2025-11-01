# Import the necessary functions for database connection.
from database.connection import get_pyodbc_connection, get_sqlalchemy_engine
from sqlalchemy import text

# This script tests the database connection and lists the tables in the database.

# Test the pyodbc connection.
print("Testing pyodbc connection...")
cnxn = get_pyodbc_connection()

# Test the SQLAlchemy engine connection.
print("\nTesting SQLAlchemy engine...")
engine = get_sqlalchemy_engine()

# Verify that the connection is successful by listing the tables in the database.
print("\nListing tables in the database...")
with engine.connect() as conn:
    # Execute a query to get the table names from the system catalog.
    result = conn.execute(text("SELECT name FROM sys.tables"))
    tables = [row[0] for row in result]
    
    # Print the list of tables.
    print("\n📊 Tables in database:")
    for t in tables:
        print(f" - {t}")
