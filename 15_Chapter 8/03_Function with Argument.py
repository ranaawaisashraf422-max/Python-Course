def goodbye(name,ending):
    print("Good Bye, "+name)
    print(ending)
goodbye("Awais","Thank You")
goodbye("Abeeha","Thank You")


#Function with Return value
def goodbye(name,ending):
    print("Good Bye, "+name)
    print(ending)
    return"done"
a = goodbye("Awais","Thank You")
print(a)
