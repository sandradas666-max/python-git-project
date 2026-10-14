
# base class Employee
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    # Display employee name and role
    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)


#Create Trainer class inheriting from Employee
class Trainer(Employee):
    def __init__(self, name, role, specialization):
        super().__init__(name, role)
        self.specialization = specialization

    # Display trainer details
    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)


#Create YogaInstructor class inheriting from Employee
class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        super().__init__(name, role)
        self.yoga_style = yoga_style

    #Display yoga instructor details
    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Yoga Style:", self.yoga_style)


#Create MultiTrainer using multiple inheritance
class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Employee.__init__(self, name, role)
        self.specialization = specialization
        self.yoga_style = yoga_style

    #Display multi-trainer details
    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)
        print("Yoga Style:", self.yoga_style)


#Create one object from each class
employee1 = Employee("Arun", "Receptionist")
trainer1 = Trainer("Sandra", "Fitness Trainer", "Weight Training")
yoga1 = YogaInstructor("Anjali", "Yoga Instructor", "Hatha Yoga")
multi1 = MultiTrainer(
    "Soorya",
    "Multi Trainer",
    "Strength Training",
    "Vinyasa Yoga"
)


#Display the details of each object
print("Employee Details")
employee1.display()

print("\nTrainer Details")
trainer1.display()

print("\nYoga Instructor Details")
yoga1.display()

print("\nMultiTrainer Details")
multi1.display()
