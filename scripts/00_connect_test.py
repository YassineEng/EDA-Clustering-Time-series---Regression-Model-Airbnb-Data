from database import get_pyodbc_connection, get_sqlalchemy_engine
from sqlalchemy import text

# Test both connections
cnxn = get_pyodbc_connection()
engine = get_sqlalchemy_engine()

# Verify tables in your database
with engine.connect() as conn:
    result = conn.execute(text("SELECT name FROM sys.tables"))
    tables = [row[0] for row in result]
    print("\n📊 Tables in database:")
    for t in tables:
        print(" -", t)
