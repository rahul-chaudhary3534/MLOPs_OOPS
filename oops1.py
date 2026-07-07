#initiate a class
class Employee:
    #special method or dunder method - constructor
    def __init__(self):
        self.id = 101
        self.salary = 950000
        self.designation = "Software Engineer"

    def travel(self, destination):
        print(f"employee is travelling to {destination}")

#create an object of the class
rahul = Employee()
#printing the attributes
print(rahul.id)
#calling the method
sam.travel("kerala")


