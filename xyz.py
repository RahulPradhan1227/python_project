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
