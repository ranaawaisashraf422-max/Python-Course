#Functions inside a class
class Employee:
    language = "Punjabi"  #This is a class Attribute.
    Salary = 1200000     
    def getinfo(self):
        print(f"The salary is {self.Salary}. The language is {self.language}")
    @staticmethod
    def greet():   #Without Self
        print("Enjoy Kro")
harry = Employee()
harry.language = "Russian"

harry.getinfo()

harry.greet()
Awais = Employee()


Awais.getinfo()