class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            return True
        return False

    def change_pin(self, old_pin, new_pin):
        if self.pin == old_pin:
            self.pin = new_pin
            self.transaction_history.append("PIN changed")
            return True
        return False

    def get_transaction_history(self):
        return self.transaction_history

class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, pin, initial_deposit=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, pin, initial_deposit)
            return True
        return False

    def authenticate(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            return account
        return None

def main():
    atm = ATM()
    
    # Create some test accounts
    atm.create_account("123456", "1234", 1000)
    atm.create_account("654321", "4321", 500)
    
    while True:
        print("\nWelcome to the ATM")
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")
        
        account = atm.authenticate(account_number, pin)
        if account:
            while True:
                print("\nATM Menu:")
                print("1. Check Balance")
                print("2. Deposit Cash")
                print("3. Withdraw Cash")
                print("4. Change PIN")
                print("5. View Transaction History")
                print("6. Exit")
                
                choice = input("Choose an option: ")
                
                if choice == "1":
                    print(f"Your balance is ${account.check_balance()}")
                
                elif choice == "2":
                    amount = float(input("Enter amount to deposit: "))
                    if account.deposit(amount):
                        print(f"${amount} deposited successfully.")
                    else:
                        print("Invalid amount.")
                
                elif choice == "3":
                    amount = float(input("Enter amount to withdraw: "))
                    if account.withdraw(amount):
                        print(f"${amount} withdrawn successfully.")
                    else:
                        print("Insufficient balance or invalid amount.")
                
                elif choice == "4":
                    old_pin = input("Enter your old PIN: ")
                    new_pin = input("Enter your new PIN: ")
                    if account.change_pin(old_pin, new_pin):
                        print("PIN changed successfully.")
                    else:
                        print("Incorrect old PIN.")
                
                elif choice == "5":
                    history = account.get_transaction_history()
                    if history:
                        print("\nTransaction History:")
                        for transaction in history:
                            print(transaction)
                    else:
                        print("No transactions found.")
                
                elif choice == "6":
                    print("Thank you for using the ATM. Goodbye!")
                    break
                
                else:
                    print("Invalid option. Please try again.")
        else:
            print("Invalid account number or PIN. Please try again.")

if __name__ == "__main__":
    main()

   
    