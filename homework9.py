
# Base class: Account
class Account:
    def __init__(self, name, balance):
        # Protected attributes
        self._name = name
        self._balance = balance

    # Special method to overload the + operator
    def __add__(self, other):
        return self._balance + other._balance


# SavingsAccount inherits from Account
class SavingsAccount(Account):
    def calculate_interest(self):
        # Calculate 5% interest
        return self._balance * 0.05


# CurrentAccount inherits from Account
class CurrentAccount(Account):
    def calculate_interest(self):
        # Calculate 2% interest
        return self._balance * 0.02


# Main program

# Create a SavingsAccount object
savings = SavingsAccount("Ravi", 10000.0)

# Create a CurrentAccount object
current = CurrentAccount("Anjali", 15000.0)


# Display SavingsAccount details
print("Savings Account Details")
print("Name:", savings._name)
print("Balance:", savings._balance)
print("Interest:", savings.calculate_interest())

print()

# Display CurrentAccount details
print("Current Account Details")
print("Name:", current._name)
print("Balance:", current._balance)
print("Interest:", current.calculate_interest())

print()

# Add both account balances using the + operator
total_balance = savings + current
print("Total Balance:", total_balance)
