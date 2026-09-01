#write a program which finds out whether a given name is present in list or not
l=["Awais", "Hussnain", "Shiblaan","Touqir"]

name=input("Enter name :")
if (name in l):
    print("Name is present in the list")
else:
    print("Name is out of list")