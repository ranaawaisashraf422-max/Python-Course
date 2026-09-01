# Write a program to filter a list of numbers which are divisible by 5.
def divisible(n):
    if(n%5==0):
        return True
    return False

a =[123,567,1245,7895,56,75,95,35]
s= list(filter(divisible,a))
print(s)

