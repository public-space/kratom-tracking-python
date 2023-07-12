
class Menu: 
    """_summary_ 
    This class is responsible for displaying the menu options and processing the user's choice
    """
    def __init__(self, auth):
        self.auth = auth
        self.authenticated = False
    # -------Menu Methods-------
    
    def display_menu(self):
        # Print the menu options
        print("======== Kratom Tracking App =======")
        print("1. Log Dose")
        print("2. View Dose Info")
        print("3. Exit")
        print("====================================")
        
    def process_menu_choices(self):
        # Process the user's choice and execute the corresponding action
        choice = input("Enter your choice: ")

        if choice == "1":
            self.log_dose()
        elif choice == "2":
            self.view_dose_info()
        elif choice == "3":
            print("Exiting the application...")
            exit()
        else:
            print("Invalid choice. Please try again.")
            
    def login_menu(self):
        while not self.authenticated:
            print("======== Login Menu =======")
            print("1. Login")
            print("2. Register")
            print("3. Exit")
            print("===========================")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.login()
            elif choice == '2':
                self.register()
            elif choice == '3':
                print("Exiting the application...")
                exit()
            else: 
                print("Invalid choice. Please try again.")
    
    def register(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        
        """
        #! THIS WAS A BUG
        #! There was a NameError here because the variable auth was not defined and called to the self, which will be called in the UserAuth Class
        #? Must be self.auth.etc...
        """
        
        user_id = self.auth.register_user(email, password)
        
        if user_id: 
            print("Registration Successful!")
            self.user_id = user_id
            self.authenticated = True
        else: 
            print("Registration failed. Please try again.")
            
            
    # -------Login Methods-------
    
    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        
        authenticated = self.auth.authenticate_user(email, password)
        
        if authenticated: 
            print("Login Successful!")
            self.user_id = self.auth.get_user_id(email)
            self.authenticated = True
        else: 
            print("Login failed. Invalid email or password")
            
     # -------Logout Methods-------
            
    def logout(self):
        self.auth.logout_user()
        self.authenticated = False
        self.user_id = None
        print("You have been logged out")

    #! -------Dose Methods-------
    
    def log_dose(self):
        if not self.authenticated:
            print("Please login to log a dose")
            return
        # TODO: Implement this method
        print("Log Dose")
    
    def view_dose_info(self):
        if not self.authenticated:
            print("Please login to view dose info")
            return
        # TODO: Implement this method
        print("View Dose Info")
        
    # TODO: Implement other methods for menu operations
