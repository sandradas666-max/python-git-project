
#Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Display person's name and age
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


#Employee class inheriting from Person
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    #Display employee details
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)


#PartTime class inheriting from Person
class PartTime(Person):
    def __init__(self, name, age, working_hours):
        super().__init__(name, age)
        self.working_hours = working_hours

    #Display part-time worker details
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Working Hours:", self.working_hours)


#Consultant class with multiple inheritance
class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        self.working_hours = working_hours
        self.project_name = project_name

    #Display consultant details
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        print("Working Hours:", self.working_hours)
        print("Project Name:", self.project_name)


#one object of each class
person1 = Person("Sandra", 25)
employee1 = Employee("Arun", 30, "EMP101")
parttime1 = PartTime("Anjali", 22, 4.5)
consultant1 = Consultant("Soorya", 28, "EMP202", 6.5, "Web Development")


#Display the details of each object
print("Person Details")
person1.show_details()

print("\nEmployee Details")
employee1.show_details()

print("\nPart-Time Worker Details")
parttime1.show_details()

print("\nConsultant Details")
consultant1.show_details()
