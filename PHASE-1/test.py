class ATM:
    def __init__(self, total_amount, user_accounts):
        self.total_amount = total_amount
        self.user_accounts = user_accounts
        self.transaction_limit = {'rupay': 2000, 'visa': 5000, 'mastercard': 8499}

    def display_remaining_amount(self):
        print(f"Remaining amount in ATM: {self.total_amount}")

    def authenticate_user(self, username, password):
        if username in self.user_accounts and self.user_accounts[username]['password'] == password:
            return True
        return False

    def check_balance(self, username):
        print(f"Your current balance is: {self.user_accounts[username]['balance']}")

    def cash_withdrawal(self, username, amount):
        card_type = self.user_accounts[username]['card_type']
        if amount > self.transaction_limit[card_type]:
            print(f"You have crossed your transaction limit for {card_type} card.")
        elif amount > self.user_accounts[username]['balance']:
            print("Insufficient balance.")
        else:
            self.user_accounts[username]['balance'] -= amount
            self.total_amount -= amount
            print(f"Transaction successful. Your new balance is: {self.user_accounts[username]['balance']}")

    def cash_deposit(self, username, amount):
        self.user_accounts[username]['balance'] += amount
        self.total_amount += amount
        print(f"Transaction successful. Your new balance is: {self.user_accounts[username]['balance']}")

    def mini_statement(self, username):
        print("Last 3 transactions:")
        for transaction in self.user_accounts[username]['transactions'][-3:]:
            print(transaction)

# User accounts data
user_accounts = {
    'user1': {'password': 'pass1', 'balance': 10000, 'card_type': 'rupay', 'transactions': []},
    'user2': {'password': 'pass2', 'balance': 15000, 'card_type': 'visa', 'transactions': []},
    'user3': {'password': 'pass3', 'balance': 20000, 'card_type': 'mastercard', 'transactions': []}
}

# Create an ATM instance with a total amount and user accounts
atm = ATM(50000, user_accounts)

# Display remaining amount in ATM
atm.display_remaining_amount()

# Authenticate user
if atm.authenticate_user('user1', 'pass1'):
    print("User authenticated successfully.")
    # Provide options to the user
    print("1. Check Balance\n2. Cash Withdrawal\n3. Cash Deposit\n4. Mini Statement")
    # User selects an option (for example, check balance)
    atm.check_balance('user1')
else:
    print("Authentication failed.")
