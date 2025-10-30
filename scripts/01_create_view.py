from sqlalchemy import text
from database.connection import get_sqlalchemy_engine

def create_views():
    engine = get_sqlalchemy_engine()

    # Read the SQL file
    with open('database/create_views.sql', 'r', encoding='utf-8') as f:
        sql_script = f.read()

    # Remove comments and empty lines, and then strip leading/trailing whitespace
    # This is a more robust way to handle SQL Server's strict requirement for CREATE VIEW
    # to be the first statement in a batch.
    import re
    
    # Remove single-line comments (--) and multi-line comments (/* ... */)
    cleaned_sql_script = re.sub(r'--.*$', '', sql_script, flags=re.MULTILINE)
    cleaned_sql_script = re.sub(r'/\*.*?\*/', '', cleaned_sql_script, flags=re.DOTALL)
    
    # Filter out empty lines but preserve content of non-empty lines
    non_empty_lines = [line for line in cleaned_sql_script.splitlines() if line.strip()]
    cleaned_sql_script = "\n".join(non_empty_lines).strip()

    print("--- Cleaned SQL Script ---")
    print(cleaned_sql_script)
    print("--------------------------")

    # Execute the SQL
    with engine.begin() as connection:  # begin() automatically handles transactions
        # Insert GO after the closing parenthesis of the CTEs and before CREATE OR ALTER VIEW
        # This ensures the CTEs are part of the first batch and CREATE VIEW is in its own batch
        sql_with_go = cleaned_sql_script.replace(")\nCREATE OR ALTER VIEW", ")\nGO\nCREATE OR ALTER VIEW")
        
        # Split the script into batches by GO and execute each batch separately
        batches = sql_with_go.split("GO")
        for batch in batches:
            batch = batch.strip()
            if batch:
                connection.execute(text(batch))

    print("✅ Views created/updated successfully.")

if __name__ == "__main__":
    create_views()
