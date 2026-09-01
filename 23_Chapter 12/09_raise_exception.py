a = int(input('Enter a Number :'))
b = int(input("Enter Second Number"))

if(b==0):
    raise ZeroDivisionError("Hey Our Program is not meant to divide numbers by zero")
else:
    print(f"The division of a / b is {a/b}")