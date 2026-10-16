
# Base class: Vehicle
class Vehicle:
    def __init__(self, vehicle_id, base_rate):
        # Protected attributes
        self._vehicle_id = vehicle_id
        self._base_rate = base_rate

    # Return the vehicle details
    def display_details(self):
        return f"Vehicle ID: {self._vehicle_id}, Base Rate: {self._base_rate:.2f}"

    # Placeholder method to be overridden by subclasses
    def rental_charge(self):
        return 0.0


# Subclass: Car
class Car(Vehicle):
    def __init__(self, vehicle_id, base_rate, num_seats):
        super().__init__(vehicle_id, base_rate)
        self.num_seats = num_seats

    # Calculate rental charge for a car
    def rental_charge(self):
        return self._base_rate * self.num_seats


# Subclass: Bike
class Bike(Vehicle):
    def __init__(self, vehicle_id, base_rate, bike_type):
        super().__init__(vehicle_id, base_rate)
        self.bike_type = bike_type

    # Calculate rental charge for a bike
    def rental_charge(self):
        return self._base_rate * 0.5


# Function demonstrating polymorphism
def calculate_rental(vehicle):
    return vehicle.rental_charge()


# Create vehicle objects
car1 = Car("CAR001", 100.00, 4)
bike1 = Bike("BIKE001", 100.00, "Scooter")

# Display vehicle details and rental charges
print(car1.display_details())
print("Car Seats:", car1.num_seats)
print(f"Car Rental Charge: {calculate_rental(car1):.2f}")

print()

print(bike1.display_details())
print("Bike Type:", bike1.bike_type)
print(f"Bike Rental Charge: {calculate_rental(bike1):.2f}")

