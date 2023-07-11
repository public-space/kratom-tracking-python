from functions.sql_handler import SQLHandler

class UserAuthenticator: 
    def __init__(self):
        self.sql_handler = SQLHandler("database/kratom.db")
        self.authenticated = False
        self.user_id = None
        
    def register_user(self, email, password):
        return self.sql_handler.insert_user(email, password)
    
    def get_user_id(self, email):
        return self.sql_handler.get_user_id_by_email(email)
    
    def authenticate_user(self, email, password):
        #TODO Check if the user exists and the password is correct
        
        #TODO Set the authentication status and user ID accordingly
        
        #TODO Return True if the user is authenticated, False Otherwise
        pass
    
    def logout_user(self):
        #TODO Reset the authentication status and user ID
        pass
        
    #! Additional Methods for user management
    
    