'''A spam comment is defined as text containing following keywords:
Make a lot of money , buy now , subscribe this , click this. Write a program to 
detect these spams '''


P1="Make a lot of money" 
P2="Buy now" 
P3="Subscribe this" 
P4="Click this"

message=input("Enter your Comment: ")
if(P1 in message) or (P2 in message) or (P3 in message):
    print("This comment is a spam")
else:
    print("This comment is not a spam")