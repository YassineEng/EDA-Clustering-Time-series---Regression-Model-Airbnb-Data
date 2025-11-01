from database import get_sqlalchemy_engine
from sqlalchemy import text

def create_table_from_view():
    engine = get_sqlalchemy_engine()
    
    # Read SQL script
    with open('database/create_table_from_view.sql', 'r') as f:
        sql_script = f.read()
    
    # Execute in a single batch
    with engine.connect() as connection:
        connection.execute(text(sql_script))
        connection.commit()
    
    print("✅ listing_features table created from view successfully.")

if __name__ == "__main__":
    create_table_from_view()
