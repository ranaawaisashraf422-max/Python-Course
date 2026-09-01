# Create a class with a class attribute a; create an object from it and set ‘a’ directly using‘object.a = 0’. Does this change the class attribute?

class Demo:
    number = 4

object = Demo()
print(object.number) #Print the cass attribute because instance one is not present

object.number = 0    #instance attribute is set

print(object.number) #Print the instance attribute because it is present

print(Demo.number)  # Print the class Attribute  