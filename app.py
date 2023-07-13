from functions.menu import Menu
from functions.user_authentication import UserAuthenticator
from functions.sql_handler import SQLHandler

def main():
    # Create and instance of SQLHandler and create the necessary tables
    sql_handler = SQLHandler("database/kratom.db")
    sql_handler.create_user_table()
    sql_handler.create_doses_table()
    
    # Pass the SQLHandler instance to UserAuthenticator
    auth = UserAuthenticator()
    menu = Menu(auth, sql_handler)
    
    while True: 
        if not menu.authenticated:
            menu.login_menu()
        else: 
            menu.display_menu()
            menu.process_menu_choices()
        
if __name__ == '__main__':
    main()