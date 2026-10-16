
from abc import ABC, abstractmethod


# 1. Create an abstract User class
class User(ABC):
    def __init__(self, name, joining_year):
        self.name = name
        self.joining_year = joining_year

    # Calculate the number of years on the platform
    def years_on_platform(self):
        return 2025 - self.joining_year

    # Abstract method to get the user's role
    @abstractmethod
    def get_role(self):
        pass

    # Special method to display user details
    def __str__(self):
        return (
            f"Name: {self.name}, "
            f"Role: {self.get_role()}, "
            f"Years on platform: {self.years_on_platform()}"
        )


# 2. Create the Customer class
class Customer(User):
    def get_role(self):
        return "Customer"


# 3. Create the Vendor class
class Vendor(User):
    def get_role(self):
        return "Vendor"


# 4. Create objects of Customer and Vendor
customer1 = Customer("Sandra", 2020)
vendor1 = Vendor("Arun", 2022)


# 5. Display the details of each user
print(customer1)
print(vendor1)

    
        
