from sqlalchemy import text
from database.connection import get_sqlalchemy_engine

def create_table_from_view():
    """
    Creates a new table from a database view.

    This function reads a SQL script from 'database/create_table_from_view.sql' 
    and executes it to create a new table named 'listing_features' from the 
    'vw_listing_features' view.
    """
    engine = get_sqlalchemy_engine()
    
    # Read the SQL script from the file.
    with open('database/create_table_from_view.sql', 'r') as f:
        sql_script = f.read()
    
    # Execute the SQL script in a single batch.
    with engine.connect() as connection:
        connection.execute(text(sql_script))
        connection.commit()
    
    print("✅ listing_features table created from view successfully.")

if __name__ == "__main__":
    # This block runs only when the script is executed directly.
    create_table_from_view()