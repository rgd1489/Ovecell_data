# app/database.py
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

class Database:
    def __init__(self):
        # Set up a PostgreSQL database connection
        self.engine = create_engine('postgresql://ovicell_user:ovicell_password@db:5432/ovicell_db')
        self.Session = sessionmaker(bind=self.engine)

    def execute(self, query, params=None):
        # Execute SQL queries on the database
        with self.engine.connect() as connection:
            result = connection.execute(query, params)
        return result

    def execute_script(self, script_path):
        # Execute SQL script files
        with open(script_path, 'r') as script_file:
            query = text(script_file.read())
            self.execute(query)
