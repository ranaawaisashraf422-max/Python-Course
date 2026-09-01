class Employee:
    company = "ITC"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
class Coder:
    language = "Python"
    def printlanguage(self):
        print(f"Out of all languages. Here is your language {self.language}")

class Programmer(Employee,Coder):
    company = "ITC infotech"
    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
a.salary = 100000
a.name = "Awais"

b=Coder()

c = Programmer()
c.name = "Rana"
c.salary = 2300000


print(a.company,c.company)

a.show()
b.printlanguage()
c.show()
c.showlanguage()