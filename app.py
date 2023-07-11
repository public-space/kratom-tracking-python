from functions.menu import Menu
from functions.user_authentication import UserAuthenticator


def main():
    menu = Menu()
    
    auth = UserAuthenticator()
    
    
    
    while True: 
        if not menu.authenticated:
            menu.show_login_menu()
        else: 
            menu.display_menu()
            menu.process_menu_choices()
        
if __name__ == '__main__':
    main()