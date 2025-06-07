balance = 0

def main():
    global balance
    print('balance:', balance)
    deposit_amount = float(input("Enter deposit amount: ").strip())
    deposit(deposit_amount)
    withdraw_amount = float(input("Enter withdrawal amount: ").strip())
    withdraw(withdraw_amount)
    print('balance:', balance)
    
def deposit(amount):
    global balance
    if amount < 0:
        raise ValueError("Deposit amount must be non-negative")
    balance += amount

def withdraw(amount):
    global balance
    if amount < 0:
        raise ValueError("Withdrawal amount must be non-negative")
    if amount > balance:
        raise ValueError("Insufficient funds")
    balance -= amount

if __name__ == "__main__":
    main()