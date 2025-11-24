import datetime

# --- BANK ACCOUNT CLASS ---
# This class handles all the saving and loading of data
class BankAccount:
    def __init__(self, name, acc_number, balance):
        self.name = name
        self.acc_number = str(acc_number)
        self.balance = balance
        
        # We will save data in a simple text file named after the account number
        # e.g., "101.txt"
        self.file_name = self.acc_number + ".txt"
        
        # CHECKING IF OLD ACCOUNT EXISTS
        # We try to open the file in 'read' mode ('r')
        try:
            with open(self.file_name, "r") as f:
                lines = f.readlines()
                # If file has lines, we get the last balance from the last line
                if len(lines) > 0:
                    last_line = lines[-1]
                    data = last_line.split(",") # splitting by comma
                    
                    # The balance is the 4th item (index 3) in our text file
                    self.balance = float(data[3])
                    print(f"\nWelcome back {self.name}!")
                    print(f"Restored Balance: {self.balance}")
        except:
            # If file doesn't exist, it goes here (New Account)
            print(f"\nCreating new account for {self.name}...")
            # Save the starting balance
            self.save_transaction("Created", balance)

    # A simple function to save data to the text file
    def save_transaction(self, type, amount):
        with open(self.file_name, "a") as f:
            # Get current time
            t = datetime.datetime.now()
            
            # Format: Time, Type, Amount, Current Balance
            # We add "\n" to go to the next line
            line = f"{t},{type},{amount},{self.balance}\n"
            f.write(line)
    
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            self.save_transaction("Deposit", amount)
            print("Success! Money Added.")
            print(f"Current Balance: {self.balance}")
        else:
            print("Error: Amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Not enough money!")
        elif amount <= 0:
            print("Error: Invalid amount.")
        else:
            self.balance = self.balance - amount
            self.save_transaction("Withdraw", amount)
            print("Success! Money taken out.")
            print(f"Current Balance: {self.balance}")

    def show_history(self):
        print("\n--- PASSBOOK PRINTING ---")
        try:
            with open(self.file_name, "r") as f:
                content = f.read()
                print(content)
        except:
            print("No history found.")
        print("-------------------------\n")

# --- MAIN PROGRAM STARTS HERE ---
# This is the part that runs when you start the game/app

print("=== WELCOME TO PYTHON BANK ===")

# Asking user for basic details
n = input("Enter your Name: ")
a = input("Enter Account Number (e.g., 101): ")
b = float(input("Enter Initial Balance: "))

# Creating the object
my_account = BankAccount(n, a, b)

# The Menu Loop
while True:
    print("\nSelect an Option:")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Print Passbook")
    print("4. Exit")
    
    choice = input("Enter choice (1-4): ")
    
    if choice == "1":
        amt = float(input("Enter amount to deposit: "))
        my_account.deposit(amt)
        
    elif choice == "2":
        amt = float(input("Enter amount to withdraw: "))
        my_account.withdraw(amt)
        
    elif choice == "3":
        my_account.show_history()
        
    elif choice == "4":
        print("Thank you for using Python Bank. Bye!")
        break # Stops the loop
        
    else:
        print("Invalid choice, please try again.")
