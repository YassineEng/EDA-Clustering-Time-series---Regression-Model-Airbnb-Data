from sqlalchemy import text
from database.connection import get_sqlalchemy_engine
import re

def create_views():
    engine = get_sqlalchemy_engine()

    # Read the SQL file
    with open('database/create_views.sql', 'r', encoding='utf-8') as f:
        sql_script = f.read()

    # Remove single-line comments (--) and multi-line comments (/* ... */)
    cleaned_sql_script = re.sub(r'--.*$', '', sql_script, flags=re.MULTILINE)
    cleaned_sql_script = re.sub(r'/\*.*?\*/', '', cleaned_sql_script, flags=re.DOTALL)

    # Remove empty lines
    non_empty_lines = [line for line in cleaned_sql_script.splitlines() if line.strip()]
    cleaned_sql_script = "\n".join(non_empty_lines).strip()

    print("--- Cleaned SQL Script ---")
    print(cleaned_sql_script)
    print("--------------------------")

    # Execute the SQL
    with engine.begin() as connection:  # begin() automatically handles transactions
        connection.execute(text(cleaned_sql_script))

    print("✅ View created/updated successfully.")

if __name__ == "__main__":
    create_views()
