from tabulate import tabulate

class Menu: 
    """_summary_ 
    This class is responsible for displaying the menu options and processing the user's choice
    """
    def __init__(self, auth, sql_handler):
        self.auth = auth
        self.authenticated = False
        self.sql_handler = sql_handler
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
        try: 
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
        except Exception as e: 
            print("Error processing choice: ", e)
            
            
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
            print("\n\nRegistration Successful!\n\n")
            self.user_id = user_id
            self.authenticated = True
            
            # After registration , automatically log the user in
            
            self.login()
            
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
            
     #! -------Logout Methods-------
            
    def logout(self):
        self.auth.logout_user()
        self.authenticated = False
        self.user_id = None
        print("You have been logged out")

    #! -------Dose Methods-------
    
    def log_dose(self):
        if not self.authenticated or self.user_id is None:
            print("Please login to log a dose")
            return
        
        # Prompt the user to enter the quantity of the dose: 
        quantity = input("Enter the quantity of the dose: ")
        
        # Attempt to convert the quantity to an integer
        try: 
            quantity = int(quantity)
        except ValueError: 
            print("Invalid quantity. Quantity must be a number.")
            return

        # Use the SQLHandler to save the dose information in the database
        self.sql_handler.insert_dose(self.user_id['id'], quantity)
    
        print('Dose logged successfully')
    
    #! -------View Dose-------
    
    def view_dose_info(self):
        if not self.authenticated:
            print("Please login to view dose info")
            return
        
       # Use the SQlHandler to retrieve dose information from the database
        doses = self.sql_handler.get_doses(self.user_id['id'])
        if not doses: 
            print("No doses logged yet")
            return
        
        #print the retrieved dose information
        print("\n============ Dose History =============\n")
        for time, quantity in doses:
            print(f"Time: {time}     |   Quantity: {quantity}  grams\n")
        
        print(tabulate(doses, headers=['Time', 'Quantity (g)'], tablefmt='fancy_grid'))
        
    # TODO: Implement other methods for menu operations
