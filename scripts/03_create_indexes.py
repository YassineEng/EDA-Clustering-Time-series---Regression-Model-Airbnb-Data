# scripts/03_create_indexes.py
from sqlalchemy import text
from database.connection import get_sqlalchemy_engine

def create_indexes():
    """
    Creates indexes on the 'listing_features' table.

    This function reads a SQL script from 'database/indexing.sql' and executes it
    to create non-clustered indexes on the 'listing_features' table. This helps
    to improve query performance.
    """
    engine = get_sqlalchemy_engine()
    
    # Load the SQL script from the file.
    with open('database/indexing.sql', 'r') as f:
        sql_script = f.read()

    # Execute the SQL script.
    with engine.connect() as conn:
        conn.execute(text(sql_script))
        conn.commit()
    
    print("✅ Indexes created successfully.")

if __name__ == "__main__":
    # This block runs only when the script is executed directly.
    create_indexes()