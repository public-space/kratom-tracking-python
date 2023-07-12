from functions.menu import Menu
from functions.user_authentication import UserAuthenticator


def main():
    
    auth = UserAuthenticator()
    menu = Menu(auth)
    
    
    
    while True: 
        if not menu.authenticated:
            menu.login_menu()
        else: 
            menu.display_menu()
            menu.process_menu_choices()
        
if __name__ == '__main__':
    main()