balance = 10000
print("ATM SIMULATOR")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")
choice = int(input("Enter your choice: "))
if choice == 1:
    print("Current Balance: ₹", balance)
elif choice == 2:
    amount = float(input("Enter amount to deposit: "))
    balance = balance + amount
    print("Deposit successful!")
    print("Updated Balance: ₹", balance)
elif choice == 3:
    amount = float(input("Enter amount to withdraw: "))
    if balance - amount >= 500:
        balance = balance - amount
        print("Withdrawal successful!")
        print("New Balance: ₹", balance)
    else:
        print("Insufficient balance!")
        print("Minimum ₹500 must remain.")
elif choice == 4:
    print("Thank you for using ATM.")
else:
    print("Invalid choice.")