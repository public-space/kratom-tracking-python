import sqlite3

class SQLHandler:
    def __init__(self, db_path):
        self.db_path = db_path
        
    def create_user_table(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
                )
                    """)
        
        connection.commit()
        connection.close()
        
        # Implement other methods for SQL operations