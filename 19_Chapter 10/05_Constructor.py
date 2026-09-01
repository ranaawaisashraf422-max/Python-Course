#Functions inside a class
class Employee:
    language = "Punjabi"  #This is a class Attribute.
    Salary = 1200000     
    def __init__(self,name,salary,language):  #dunder Method which is automatically called

        self.name = name
        self.salary = salary
        self.language = language
        print("I'm creating an object")
    def getinfo(self):
        print(f"The salary is {self.Salary}. The language is {self.language}")

    @staticmethod
    def greet():   #Without Self
        print("Enjoy Kro")

harry = Employee("Rana", 1300000, "German")
#harry.name="Awais"
print(harry.name,harry.Salary)

Awais=Employee("Awais",5000000,"Urdu")
Awais.getinfo()