'''
Write a python program using function to convert Celsius to Fahrenheit.
'''

def celsius_to_Farenheit(celsius):
    farenheit = (celsius*9/5) + 32
    return farenheit
c= int(input("Enter Temperature in celsius :"))
f=celsius_to_Farenheit(c)
print(f"{round(f,2)} F")


