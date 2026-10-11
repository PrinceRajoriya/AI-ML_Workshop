class BankAccount:
    def __init__(self, account_number, account_holder, account_type, balance, minimum_balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_type = account_type
        self.balance = balance
        self.minimum_balance = minimum_balance
        self.transaction_history = []  # Starts as an empty list

    def deposit(self, amount):
        # Condition: Deposit must be greater than 0
        if amount <= 0:
            print("Error: Deposit amount must be greater than 0.")
            return

        # Add money to balance
        self.balance = self.balance + amount
        
        # Record successful transaction
        self.transaction_history.append(f"Deposited: {amount}")
        
        # Display updated balance
        print(f"Success! New Balance: {self.balance}")

    def withdraw(self, amount):
        # Condition: Cannot withdraw more than you have
        if amount > self.balance:
            print("Error: Not enough money in account.")
            return

        # Condition: Balance cannot fall below the minimum required balance
        if (self.balance - amount) < self.minimum_balance:
            print(f"Error: Must keep at least {self.minimum_balance} in the account.")
            return

        # Subtract money from balance
        self.balance = self.balance - amount
        
        # Record successful transaction
        self.transaction_history.append(f"Withdrew: {amount}")
        
        # Display updated balance
        print(f"Success! New Balance: {self.balance}")

    def check_balance(self):
        print(f"Your current balance is: {self.balance}")

    def display_account_details(self):
        print("--- Account Details ---")
        print(f"Number: {self.account_number}")
        print(f"Holder: {self.account_holder}")
        print(f"Type: {self.account_type}")
        print(f"Balance: {self.balance}")
        print(f"Minimum Required: {self.minimum_balance}")

    def show_transaction_history(self):
        print("--- Transaction History ---")
        for transaction in self.transaction_history:
            print(transaction)


# --- Testing the code in a simple way ---

# 1. Create a new account
my_account = BankAccount("123456", "Alex Smith", "Savings", 5000, 1000)

# 2. Show the details
my_account.display_account_details()

# 3. Try depositing money
print("\nTrying to deposit 500:")
my_account.deposit(500)

# 4. Try withdrawing money safely
print("\nTrying to withdraw 2000:")
my_account.withdraw(2000)

# 5. Try breaking the rules (withdrawing too much)
print("\nTrying to withdraw 4000 (Should fail due to minimum balance):")
my_account.withdraw(4000)

# 6. Look at the history of what happened
print("\nShowing history:")
my_account.show_transaction_history()
