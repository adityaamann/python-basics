class ATM:
#static variable
    __counter = 1


    def __init__(self, balance=0, pin=1234):
        #instance variables
        self.__balance = balance
        self.__pin = pin
        self.sNo = ATM.__counter
        ATM.__counter = ATM.__counter + 1
        print(f"🎯 Account created successfully! Account No: {self.sNo}")

    
    def __verify_pin(self):
        entered_pin = int(input("Enter your PIN: "))  
        if entered_pin == self.__pin:
            print("✅ Correct PIN")
            return True
        else:
            print("❌ Incorrect PIN")
            return False

    # Check balance
    def check_balance(self):
        if self.__verify_pin():   
            print(f"💰 Your current balance is: ₹{self.__balance}")

    # Deposit money
    def deposit(self):
        if self.__verify_pin():
            amount = float(input("Enter amount to deposit: "))  
            if amount > 0:
                self.__balance += amount
                print(f"✅ Deposited ₹{amount}. New balance: ₹{self.__balance}")
            else:
                print("❌ Invalid amount")

    # Withdraw money
    def withdraw(self):  
        if self.__verify_pin():
            amount = float(input("Enter amount to withdraw: "))  
            if amount <= 0:
                print("❌ Invalid amount")
            elif amount > self.__balance:
                print("❌ Insufficient balance")
            else:
                self.__balance -= amount
                print(f"✅ Withdrawn ₹{amount}. New balance: ₹{self.__balance}")

    # Change PIN
    def change_pin(self):
        if self.__verify_pin():
            new_pin = int(input("Enter new PIN: "))  
            self.__pin = new_pin
            print("✅ PIN changed successfully!")

    def get_balance(self):
        return self.__balance

    def get_pin(self):
        return self.__pin


# ---- Using the ATM class ----
my_account = ATM(1000, 1234)

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Check PIN")
    print("6. Check Balance")
    print("7. Exit")


    choice = int(input("Enter your choice: "))

    if choice == 1:
        my_account.check_balance()
    elif choice == 2:
        my_account.deposit()
    elif choice == 3:
        my_account.withdraw()
    elif choice == 4:
        my_account.change_pin()
    elif choice == 5:
        print(f"🔑 Your current PIN is: {my_account.get_pin()}")
    elif choice == 6:
        my_account.check_balance()
    elif choice == 7:
        print("🙏 Thank you for using the ATM!")
        break
    else:
        print("❌ Invalid choice, try again.")

