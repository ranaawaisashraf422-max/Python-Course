class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "ITC infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showlanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")
 #With Inheritance
class Programmer(Employee):
    company = "ITC infotech"
    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
a.salary = 100000
a.name = "Awais"

b = Programmer()
b.name = "Rana"
b.salary = 2300000
b.language = "JavaScript"

print(a.company,b.company)

a.show()
b.show()
b.showlanguage()