# Write a program to find the maximum of the numbers in a list using the reduce function
from functools import reduce
a =[1,2,3,567,12,78,56,75,95,35]
def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,a))
