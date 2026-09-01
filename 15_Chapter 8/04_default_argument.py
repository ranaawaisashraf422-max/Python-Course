def goodbye(name,ending="Thank You"):
    print("Good Bye," + name)
    print(ending)
goodbye("Awais","Thanks")
goodbye("Abeeha",)

#Example 

def greet(name = "stranger"):
    print(f"Good Day, {name}")

greet() # name will be "stranger" in function body (default)
greet("Awais")
