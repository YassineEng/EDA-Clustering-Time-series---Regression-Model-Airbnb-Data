# scripts/06_create_indexes.py
from database.connection import get_sqlalchemy_engine
from sqlalchemy import text

def create_indexes():
    engine = get_sqlalchemy_engine()
    
    # Load SQL script
    with open('database/indexing.sql', 'r') as f:
        sql_script = f.read()

    # Execute the SQL
    with engine.connect() as conn:
        conn.execute(text(sql_script))
        conn.commit()
    
    print("✅ Indexes created successfully.")

if __name__ == "__main__":
    create_indexes()
