a = int(input("Enter your age :"))
#If statement no 1
if(a%2==0):
    print("age is even")
#End of Statement No 2

#If statement no 2
if(a>=18):
    print("You are above the age of concent")
    print("Good For You")
elif(a<0):
    print("You are entering an invalid negative age")
elif(a==0):
    print("You are entering 0 which is not valid age")

else:
    print("You are below the age of concent")
print("End of Program")