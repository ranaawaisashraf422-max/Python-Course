'''Write a program to calculate the grade of student from his marks from the
following scheme
90 -100 (Ex)
80 - 90  (A)
70 - 80  (B)
60 - 70  (C)   
50 - 60  (D)
  <50    (F)
  '''
marks=int(input("Enter your marks: "))
if(marks<=100 and marks>=90):
    Grade="Ex"
elif(marks<=100 and marks>=90):
    Grade="A"
elif(marks<=90 and marks>=80):
    Grade="B"
elif(marks<=80 and marks>=70):
    Grade="C"
elif(marks<=70 and marks>=60):
    Grade="D"
elif(marks<=60 and marks>=50):
    Grade="E"
elif(marks<50 ):
    Grade="F"

print("Your Grade is",Grade)