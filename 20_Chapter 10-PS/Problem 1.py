# Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,postal_code):
        self.name = name
        self.salary = salary
        self.postal_code = postal_code


p = Programmer("Awais",5000000,37300)
print(p.name,p.salary,p.postal_code,p.company)

r = Programmer("Abeeha",2500000,37300)
print(r.name,r.salary,r.postal_code,r.company)