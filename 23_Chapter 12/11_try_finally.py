try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as e:
    print(e)

finally:
    print("I'm inside of finally")

#So the main here is that if we don't use finally then on print statement program will be run successfully and print that statement without finally. Because finally statement has to be run confirmly in try case or except case.

#So what wil be the difference here . We know that in case of function if we run a function then only function is run on time of execution. But with finally statement; we can run finnaly block code even we run func_.
def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)

    except Exception as e:
        print(e)

    else:
        print("I'm inside else")

main()


