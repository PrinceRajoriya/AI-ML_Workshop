account_number = (123,245,364)
account_holder = ("Prince", "priyanshu", "aditya")
account_type = ("Saving","Current")
balance = (10000,20000,30000)
minimum_balance = (500,1000,1500)
transaction_history = (["Deposit: 1000", "Withdrawal: 500"], ["Deposit: 2000", "Withdrawal: 1000"], ["Deposit: 3000", "Withdrawal: 1500"],)

deposited_amount = float(transaction_history[0][0].split(": ")[1])
print("Deposited_amount:", deposited_amount)
withdrawn_amount = float(transaction_history[0][1].split(": ")[1])
print("Withdrawn_amount:", withdrawn_amount)
print("Check_balance:", balance[0])
display_account_details = f"""Account Number: {account_number[0]} Account Holder: {account_holder[0]} Account Type: {account_type[0]}"""
print("Account_Details:", display_account_details)
show_transaction_history = f"""Transaction History: {transaction_history[0]}"""
print("Transaction_History:", show_transaction_history)