#lenght function
name="Awais"
print(len(name))

# ends/starts function
name = "Abeeha"
Tail= name.endswith("ha")
print(Tail)
Invastigate = name.startswith("Ab")
print(Invastigate)

# Upper/Lower Function
name = "Shahida"
Major = name.upper()
Minor = name.lower()
print(Major)
print(Minor)

#Title function
Course="discrete mathematics"
Modify= Course.title()
print(Modify)

#Capitalize Function
Movie="century girl"
print(Movie.capitalize())

#Count Function
Fruit= "Banana"
print(Fruit.count("n"))

# Swapcase Function
College= ("ChrIsTian CoLleGe")
print(College.swapcase())

#strip function
string = "    Calculas  "
print(string.strip())

#rstrip/lstrip
Bird= "     Parrot      "
Animal= "   Cow        "
print(Bird.lstrip())
print(Animal.rstrip())

#replace function
text="I am in relationship"
print(text.replace("relationship","Imagineship"))

# find Function
string = "My Name is Awais"
print(string.find("Name"))

#Index Function
text="What is your name?"
print(text.index("name"))

#Split Function
name=("Wait or Fate")
print(name.split())

#Join Function
City=("Samundri","Faisalabad","Islamabad")
print(" ".join(City))

#isalpha function
Village="Kaakywaa"
print(Village.isalpha())

#isdight function
postal_code="37300"
print(postal_code.isdigit())

#is alnum function
Address="Chak533gb"
print(Address.isalnum())

#isspace function
Story=" "
print(Story.isspace())

#center function
name="RAJPUT"
print(name.center(15,"*"))

#Zfill Function
text="Awais"
print(text.zfill(15))

#casefold function
name="KARACHI"
print(name.casefold())

#removeprefix function
Owner="Mr.Sadiq"
print(Owner.removeprefix("Mr."))

#removesuffix function
Extension= "Pyhton.py"
print(Extension.removesuffix(".py"))