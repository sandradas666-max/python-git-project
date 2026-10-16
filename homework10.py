
from abc import ABC, abstractmethod


# 1. Create an abstract User class
class User(ABC):

    # Constructor to store the user's name and account creation year
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year

    # Concrete method to calculate account age
    def account_age(self):
        return 2025 - self.account_year

    # Abstract method that subclasses must implement
    @abstractmethod
    def get_role(self):
        pass


# 2. Create the Admin subclass
class Admin(User):

    # Return the role of the user
    def get_role(self):
        return "Admin"

    # Magic method to display a user-friendly message
    def __str__(self):
        return (
            f"User: {self.name}, "
            f"Role: {self.get_role()}, "
            f"Account Age: {self.account_age()} years"
        )


# 3. Create the Guest subclass
class Guest(User):

    # Return the role of the user
    def get_role(self):
        return "Guest"

    # Magic method to display a user-friendly message
    def __str__(self):
        return (
            f"User: {self.name}, "
            f"Role: {self.get_role()}, "
            f"Account Age: {self.account_age()} years"
        )


# 4. Create objects of both subclasses
admin1 = Admin("Sandra", 2020)
guest1 = Guest("Arun", 2023)


# 5. Print the role, account age, and object message
print("Admin Role:", admin1.get_role())
print("Admin Account Age:", admin1.account_age())
print(admin1)

print()

print("Guest Role:", guest1.get_role())
print("Guest Account Age:", guest1.account_age())
print(guest1)
