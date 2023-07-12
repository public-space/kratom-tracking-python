from functions.menu import Menu
from functions.user_authentication import UserAuthenticator
from functions.sql_handler import SQLHandler

def main():
    
    sql_handler = SQLHandler("database/kratom.db")
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