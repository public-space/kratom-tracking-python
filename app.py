from functions.menu import Menu

def main():
    menu = Menu()
    
    while True: 
        menu.display_menu()
        menu.process_menu_choices()
        
if __name__ == '__main__':
    main()