class Menu: 
    def __init__(self):
        #initialize and necessary attributes
        pass
    
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
    
    def log_dose(self):
        #TODO Implement this method
        print("Log Dose")
    
    def view_dose_info(self):
        #TODO Implement this method
        print("View Dose Info")
        
    #TODO Implement other methods for menu operations