class Employee:
    a = 1
class Programmer(Employee):
    b = 2
class Manager(Programmer):
    c = 3

A = Employee()
print(A.a) # Prints an attribute a
#print(A.b) # Shows an error brcause there is no attribute b in Employee class


A = Programmer()
print(A.a,A.b)


A = Manager()
print(A.a,A.b,A.c)