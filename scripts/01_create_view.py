import re
from sqlalchemy import text
from database.connection import get_sqlalchemy_engine

def create_views():
    """
    Creates or updates a database view from a SQL script.

    This function reads a SQL script from 'database/create_views.sql', cleans it by removing
    comments and empty lines, and then executes it to create or update a view.
    """
    engine = get_sqlalchemy_engine()

    # Read the SQL file.
    with open('database/create_views.sql', 'r', encoding='utf-8') as f:
        sql_script = f.read()

    # Remove single-line (--) and multi-line (/* ... */) comments.
    cleaned_sql_script = re.sub(r'--.*$', '', sql_script, flags=re.MULTILINE)
    cleaned_sql_script = re.sub(r'/\*.*?\*/', '', cleaned_sql_script, flags=re.DOTALL)

    # Remove any empty lines to ensure the script is clean.
    non_empty_lines = [line for line in cleaned_sql_script.splitlines() if line.strip()]
    cleaned_sql_script = "\n".join(non_empty_lines).strip()

    print("--- Cleaned SQL Script ---")
    print(cleaned_sql_script)
    print("--------------------------")

    # Execute the SQL script in a transaction.
    with engine.begin() as connection:
        connection.execute(text(cleaned_sql_script))

    print("✅ View created/updated successfully.")

if __name__ == "__main__":
    # This block runs only when the script is executed directly.
    create_views()