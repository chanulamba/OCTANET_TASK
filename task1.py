class ATM:
    def __init__(self):
        self.balance = 10000  
    def display_menu(self):
        print("ATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Transfer Funds")
        print("5. Transaction History")
        print("6. Quit")

    def check_balance(self):
        print(f"Your current balance is ${self.balance}")

    def withdraw_money(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Your new balance is ${self.balance}")
        else:
            print("Insufficient funds.")

    def deposit_money(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Your new balance is ${self.balance}")

    def transfer_funds(self, amount, recipient_account):
        if amount <= self.balance:
            self.balance -= amount
            recipient_account.balance += amount
            print(f"Transferred ${amount} to {recipient_account}.")
        else:
            print("Insufficient funds.")

    # def transaction_history(self):
    #     print("Transaction History:")
    #     # Implement logic to display transaction history

    def run(self):
        print("Welcome to the Python ATM!")
        user_id = input("Enter your user ID: ")
        pin = input("Enter your PIN: ")

        if user_id == "12345" and pin == "1234":  
            print("Authentication successful. You can now perform transactions.")
            while True:
                self.display_menu()
                choice = input("Enter your choice: ")
                if choice == "1":
                    self.check_balance()
                elif choice == "2":
                    amount = float(input("Enter the withdrawal amount: $"))
                    self.withdraw_money(amount)
                elif choice == "3":
                    amount = float(input("Enter the deposit amount: $"))
                    self.deposit_money(amount)
                elif choice == "4":
                    recipient_account = input("Enter recipient's account number: ")
                    amount = float(input("Enter the transfer amount: $"))
                    self.transfer_funds(amount, recipient_account)
                elif choice == "5":
                    self.transaction_history()
                elif choice == "6":
                    print("Thank you for using the Python ATM. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")


if __name__ == "__main__":
    atm = ATM()
    atm.run()
