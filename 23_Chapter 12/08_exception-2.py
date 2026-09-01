try:
    a = int(input("Enter a number :"))
    b = int(input("Enter a number :"))
    print(a / b)

except ZeroDivisionError:
    print("Error! Yoy can't divide by zero.")

except TypeError:
    print("Error! Wrong data type")

except:
    print("Some other error has been occured!")