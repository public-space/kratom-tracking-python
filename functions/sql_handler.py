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
        
        
    def view_tables(self):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        
        print("Tables: ")
        for table in tables: 
            print("- ", table[0])
            
        connection.close()
            
    #TODO Implement other methods for SQL operations