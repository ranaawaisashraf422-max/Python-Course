#a = int(input("Hey, Enter a number: "))
#print(a)

#After run it my this program will be crash if i will give invalid entry like string or int or anything instead if int.

# For this we will use try-except,  where program say not to crash(not shoe error)

try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as e:
    print(e)


print("Nahi hai Error! Bhai")

