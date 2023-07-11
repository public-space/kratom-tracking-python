import sqlite3
import hashlib

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
        
    def insert_user(self, email, password):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        
        # Hash the password before storing it
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        try: 
            cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed_password))
            connection.commit()
            return True
        except sqlite3.Error as e: 
            print("Error inserting user: ", e)
            
        connection.close()
        return False
        
    def get_user_id_by_email(self, email):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        
        cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
        
        user_id = cursor.fetchone()
        
        connection.close()
        
        if user_id is None: 
            return None
        else: 
            return user_id[0]
            
    #TODO Implement other methods for SQL operations