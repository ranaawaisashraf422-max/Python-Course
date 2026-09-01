# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

from random import randint
class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo
        pass
    def book(self,fro,to):
        print(f"Ticket is booked in train No : {self.trainNo} From {fro} to {to}")
    def getstatus(self):
        print(f"Train no: {self.trainNo} is running on time")
    def getfare(self,fro,to):
        print(f"Ticket Fare in train No {self.trainNo} From {fro} to {to} is {randint(222,555)}")

t = Train(24522)

t.book("Faisalabd","Karachi")
t.getstatus()
t.getfare("Faisalabd","Karachi")