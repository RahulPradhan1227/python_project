# import datetime  # Imported to add timestamps to the file

# class Account:
#     def _init_(self, bal, acc, acc_pass):
#         self.bal = bal
#         self.acc = acc
#         self.acc_pass = acc_pass
#         # Create a unique filename for this account
#         self.filename = f"Statement_{self.acc}.txt"

#     # --- NEW METHOD: Handles writing to the file ---
#     def log_transaction(self, trans_type, amount):
#         # 'a' mode opens the file for appending (adding to the end)
#         with open(self.filename, "a") as f:
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             # Write: Date | Type | Amount | Final Balance
#             f.write(f"[{timestamp}] {trans_type}: Rs.{amount} | Balance: Rs.{self.bal}\n")
#         print(f"Transaction saved to {self.filename}")

#     def debit(self, debit_amt):
#         # Only ask for inputs if you really need to re-authenticate every time
#         x = int(input("\n-- DEBIT REQUEST --\nEnter account number: "))
#         y = int(input("Enter account password: "))
        
#         if x == self.acc and y == self.acc_pass:
#             if self.bal - debit_amt < 0:
#                 print("Insufficient balance")
#             else:
#                 self.bal -= debit_amt
#                 print(f"Rs. {debit_amt} debited. Remaining balance: {self.bal}")
#                 # Call the log function
#                 self.log_transaction("DEBIT", debit_amt)
#         else:
#             print("Authentication Failed.")

#     def credit(self, credit_amt):
#         x = int(input("\n-- CREDIT REQUEST --\nEnter account number: "))
#         y = int(input("Enter account password: "))
        
#         if x == self.acc and y == self.acc_pass:
#             self.bal += credit_amt
#             print(f"Rs. {credit_amt} credited. Remaining balance: {self.bal}")
#             # Call the log function
#             self.log_transaction("CREDIT", credit_amt)
#         else:
#             print("Authentication Failed.")

#     def get_balance(self):
#         return self.bal

# # --- Usage ---
# s1 = Account(10000, 1234, 100)

# # These will prompt you for inputs (1234 and 100)
# s1.debit(2000) 
# s1.credit(500) 
# s1.debit(222222) # This will fail (insufficient funds) but won't log logic unless you add it




# class Account:
#     def _init_(self,bal ,acc,acc_pass):
#         self.bal = bal
#         self.acc = acc
#         self.acc_pass = acc_pass
    
#     def d(self,debit):
#         x = int(input("Enter account number :"))
#         y = int(input("Enter account password :"))
#         if self.bal - debit < 0 :
#             print("insufficient balance")    
#         else:
#             if x == self.acc and y == self.acc_pass :
#                 self.bal -= debit
#                 print("RS.",debit,"debited from your account","remaining balance is ",self.r())
#             else:
#                 print("something went wrong....")
#     def c(self,credit):
#         x = int(input("Enter account number :"))
#         y = int(input("Enter account password :"))
#         if x == self.acc and y == self.acc_pass:
#             self.bal += credit
#             print("RS.",credit,"credited from your account","remaining balance is ",self.r())
#         else:
#             print("something went wrong..")

#     def r(self):
#         return self.bal

# s1 = Account(10000,1234,100)
# s1.d(2000)
# s1.c(262)
# s1.d(222222)



# t datetime

# class Account:
#     def _init_(self, acc, acc_pass, initial_bal=0):
#         self.acc = acc
#         self.acc_pass = acc_pass
#         self.filename = f"Statement_{self.acc}.csv"
        
#         # Check if file exists. If NOT, create it and add Headers.
#         if not os.path.exisimport csv
# import os
# imports(self.filename):
#             with open(self.filename, mode='w', newline='') as file:
#                 writer = csv.writer(file)
#                 # Writing the Header Row
#                 writer.writerow(["Timestamp", "Transaction Type", "Amount", "Balance"])
#             self.bal = initial_bal
#             print(f"New account created. Starting Balance: Rs.{self.bal}")
#         else:
#             # If file exists, load the last balance
#             self.bal = self.get_last_balance()
#             print(f"Welcome back! Balance restored: Rs.{self.bal}")

#     def log_transaction(self, trans_type, amount):
#         """Appends a new row to the CSV file."""
#         with open(self.filename, mode='a', newline='') as file:
#             writer = csv.writer(file)
#             timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             # Write the data as a list
#             writer.writerow([timestamp, trans_type, amount, self.bal])
    
#     def get_last_balance(self):
#         """Reads the CSV to find the balance in the very last row."""
#         try:
#             with open(self.filename, mode='r') as file:
#                 reader = csv.reader(file)
#                 data = list(reader) # Convert all rows to a list
                
#                 # Check if there is data beyond the header (length > 1)
#                 if len(data) > 1:
#                     last_row = data[-1] # Get the last list item
#                     # Balance is at index 3 (0=Time, 1=Type, 2=Amt, 3=Bal)
#                     return float(last_row[3]) 
#                 else:
#                     return 0 # Only header exists
#         except Exception as e:
#             print("Error reading file:", e)
#             return 0

#     def debit(self, amount):
#         # (Simplified for brevity - assuming authentication matches)
#         if self.bal >= amount:
#             self.bal -= amount
#             print(f"Debited {amount}. New Balance: {self.bal}")
#             self.log_transaction("DEBIT", amount)
#         else:
#             print("Insufficient Balance")

#     def credit(self, amount):
#         self.bal += amount
#         print(f"Credited {amount}. New Balance: {self.bal}")
#         self.log_transaction("CREDIT", amount)

# # --- USAGE ---
# s1 = Account(1234, 100, 10000)
# s1.debit(2000)
# s1.credit(500)


import csv
import os
import datetime

class Account:
    def _init_(self, acc_no, password, name="", initial_bal=0):
        self.acc_no = str(acc_no)
        self.password = password
        self.name = name
        self.filename = f"database/Statement_{self.acc_no}.csv"
        os.makedirs("database", exist_ok=True)

        if not os.path.exists(self.filename):
            with open(self.filename, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "Transaction Type", "Amount", "Balance", "Description"])
            self.balance = initial_bal
            self.log_transaction("CREDIT", initial_bal, "Account Created")
            print(f"Account {acc_no} created successfully!")
        else:
            self.balance = self.get_last_balance()
            print(f"Welcome back {name}! Current Balance: ₹{self.balance}")

    def log_transaction(self, trans_type, amount, desc=""):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, trans_type, amount, self.balance, desc])

    def get_last_balance(self):
        try:
            with open(self.filename, 'r') as f:
                rows = list(csv.reader(f))
                if len(rows) > 1:
                    return float(rows[-1][3])
                else:
                    return 0.0
        except:
            return 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive!")
            return False
        self.balance += amount
        self.log_transaction("CREDIT", amount)
        print(f"₹{amount} Deposited | New Balance: ₹{self.balance}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
            return False
        if self.balance >= amount:
            self.balance -= amount
            self.log_transaction("DEBIT", amount)
            print(f"₹{amount} Withdrawn | Remaining: ₹{self.balance}")
            return True
        else:
            print("Insufficient Balance!")
            return False

    def transfer(self, to_acc, amount):
        if self.withdraw(amount, f"Transfer to {to_acc.acc_no}"):
            to_acc.deposit(amount, f"Transfer from {self.acc_no}")
            print("Transfer Successful!")
            return True
        return False

    def show_statement(self):
        print(f"\n{'='*60}")
        print(f"STATEMENT FOR ACCOUNT: {self.acc_no} ({self.name})")
        print(f"{'='*60}")
        try:
            with open(self.filename, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    print(f"{row[0]} | {row[1]:<8} | ₹{row[2]:<10} | Bal: ₹{row[3]} | {row[4]}")
        except:
            print("No transactions yet.")
            
s1 = Account("1234",100,"rahul",100000)
s1.withdraw(999)
s1.show_statement()