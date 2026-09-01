class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1
class Programmer(Employee):
    def __init__(self):
            print("Constructor of Programmer")
    b = 2
class Manager(Programmer):
    def __init__(self):
            super().__init__()
            print("Constructor of Manager")
    c = 3

# A = Employee()
# print(A.a) # Prints an attribute a
#print(A.b) # Shows an error brcause there is no attribute b in Employee class


# A = Programmer()
# print(A.a,A.b)


A = Manager()
print(A.a,A.b,A.c)

# When i Execute only object of Programmer then its Constructor is print. This will be done for other tooo also.

#But if i want to print the constructor of parent class along with its child class then i will use super() in child class.