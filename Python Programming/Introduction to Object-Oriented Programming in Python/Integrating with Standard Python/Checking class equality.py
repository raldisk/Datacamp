class BankAccount:
    def __init__(self, number, balance=0):
        self.number, self.balance = number, balance

    def withdraw(self, amount):
        self.balance -= amount

    # Modify to add a check for the class type
    def __eq__(self, other):
        return (self.number == other.number) and (type(self) == type(other))


acct = BankAccount(873555333)
pn = Phone(873555333)

# Check if the two objects are equal
print(acct == pn)
