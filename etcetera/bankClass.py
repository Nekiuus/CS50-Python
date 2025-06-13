class Account():
    def __init__(self, name, balance=0):
        self.name = name
        self._balance = balance
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

def main():
    account = Account("Jane Doe", 100)
    print(f"Account holder: {account.name}")
    print(f"Initial balance: ${account.balance}")
    account.deposit(500)
    account.withdraw(200)
    print(f"Balance after transactions: ${account.balance}")


if __name__ == "__main__":
    main()

   