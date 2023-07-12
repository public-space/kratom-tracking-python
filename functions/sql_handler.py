import sqlite3
import hashlib

class SQLHandler:
    """_summary_
    This class is responsible for handling SQL operations
    """
    def __init__(self, db_path):
        self.db_path = db_path
        
    #!------ USER TABLE METHODS ------
    
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
        
        query = "SELECT id, password FROM users WHERE email = ?"
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        
        connection.close()
        
        if result is None:
            return None
        
        user = {
            'id': result[0],
            'password': result[1]
        }
        
        return user
    
    #!------ DOSE TABLE METHODS ------
    def create_doses_table(self):
        #Establish a connection to the database and create a cursor
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        
        #Execute a SQL query to create the doses table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS doses (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                user_id INTEGER NOT NULL,
                time DATETIME NOT NULL, 
                quantity INTEGER NOT NULL, 
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
            """)
        
        # Commit the changes and close the connection
        connection.commit()
        connection.close()
        
    def insert_dose(self, user_id, time, quantity):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        
        # Execute a SQL query to insert a dose into the doses table
        cursor.execute("""
            INSERT INTO doses (user_id, time, quantity)
            VALUES (?, datetime('now'), ?)
            """, (user_id, quantity))
        
        connection.commit()
        connection.close()
        
    def get_doses(self, user_id):
        connection = sqlite3.connect(self.db_path)
        cursor = connection.cursor()
        
        #Execute a SQL query to retrieve all doses for a user
        cursor.execute("""
            SELECT id, time, quantity
            FROM doses
            WHERE user_id = ?           
            """, (user_id,))
        
        # Fetch all the results from the query
        doses = cursor.fetchall()
        
        # Close the connection
        connection.close()
        
        #Return the retrieved doses
        return doses
        
    
      
    #TODO Implement other methods for SQL operations