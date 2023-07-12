from functions.sql_handler import SQLHandler
import hashlib

class UserAuthenticator: 
    """_summary_
    This class is responsible for authenticating users and managing user accounts
    """
    
    def __init__(self):
        self.sql_handler = SQLHandler("database/kratom.db")
        self.authenticated = False
        self.user_id = None
        
    def register_user(self, email, password):
        return self.sql_handler.insert_user(email, password)
    
    def get_user_id(self, email):
        return self.sql_handler.get_user_id_by_email(email)
    
    def authenticate_user(self, email, password):
        user = self.sql_handler.get_user_id_by_email(email)
        
        if user is not None:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            
            if user['password'] == hashed_password:
                self.authenticated = True
                self.user_id = user['id']
                return True
            
            return False

        
        
    def logout_user(self):
        self.authenticated = False
        self.user_id = None
        
    #! Additional Methods for user management
    
    