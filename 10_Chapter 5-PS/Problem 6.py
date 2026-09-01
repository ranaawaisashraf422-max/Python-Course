'''
Create an empty dictionary. Allow 4 friends to enter their favourite language
as value and key as their names. Assume that the names are unique.'''

d={}
name = input("Enter Friend Name: ")
lang = input("Enter language Name: ")
d.update({name:lang})

name = input("Enter Friend Name: ")
lang = input("Enter language Name: ")
d.update({name:lang})
name = input("Enter Friend Name: ")
lang = input("Enter language Name: ")
d.update({name:lang})
name = input("Enter Friend Name: ")
lang = input("Enter language Name: ")
d.update({name:lang})

print(d)
