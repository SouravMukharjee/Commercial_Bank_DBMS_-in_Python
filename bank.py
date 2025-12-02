class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: ${self.balance}")

# Main program
def main():
    accounts = []
    while True:
        print("\n--- Commercial Bank Management System ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Account Info")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            acc_num = input("Enter account number: ")
            name = input("Enter customer name: ")
            accounts.append(BankAccount(acc_num, name))
            print("Account created successfully!")
        elif choice == "2":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            for acc in accounts:
                if acc.account_number == acc_num:
                    acc.deposit(amount)
                    break
            else:
                print("Account not found!")
        elif choice == "3":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            for acc in accounts:
                if acc.account_number == acc_num:
                    acc.withdraw(amount)
                    break
            else:
                print("Account not found!")
        elif choice == "4":
            acc_num = input("Enter account number: ")
            for acc in accounts:
                if acc.account_number == acc_num:
                    acc.display()
                    break
            else:
                print("Account not found!")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
