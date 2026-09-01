'''
Write a program using functions to find greatest of three numbers.
'''

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c


print(greatest(56,67,78))