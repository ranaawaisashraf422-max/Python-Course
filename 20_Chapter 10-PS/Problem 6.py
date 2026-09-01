# Can you change the self-parameter inside a class to something else (say “harry”)? Try changing self to “slf” or “harry” and see the effects.

from random import randint
class Train:
    def __init__(slf,trainNo):
        slf.trainNo = trainNo
        pass
    def book(harry,fro,to):
        print(f"Ticket is booked in train No : {harry.trainNo} From {fro} to {to}")
    def getstatus(harry):
        print(f"Train no: {harry.trainNo} is running on time")
    def getfare(harry,fro,to):
        print(f"Ticket Fare in train No {harry.trainNo} From {fro} to {to} is {randint(222,555)}")

t = Train(24522)

t.book("Faisalabd","Karachi")
t.getstatus()
t.getfare("Faisalabd","Karachi")