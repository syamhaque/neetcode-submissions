class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0    # Class attribute: Shared by ALL accounts
    total_balance = 0     # Class attribute: Tracks bank's total money
    
    def __init__(self, name: str, balance: float):
        self.name = name        # Instance: Each account has unique owner
        self.balance = balance  # Instance: Each account has unique balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance


# TODO: Create two accounts
bank_account1 = BankAccount("Alice", 1000)
bank_account2 = BankAccount("Bob", 2000)
# TODO: Print the information using the mentioned format
print(f"{bank_account1.name}'s balance: ${bank_account1.balance}")
print(f"{bank_account2.name}'s balance: ${bank_account2.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")