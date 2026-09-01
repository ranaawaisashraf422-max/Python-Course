'''
Write a program to find wheather a student has passed or failes if it requires
a total of 40% and 33% in each subject to pass. Assume 3 subjects and marks as
an input from the user'''

marks_1=int(input("Enter Subject 1 marks :"))
marks_2=int(input("Enter Subject 2 marks :"))
marks_3=int(input("Enter Subject 3 marks :"))

#Check for total percantage
total_percantage=(100*(marks_1+marks_2+marks_3))/300

if(total_percantage>=40 and marks_1>=33 and marks_2>=33 and marks_3>=33):
    print("You are Passed! Congratulations", total_percantage)

else:
    print("You are failed! Good Luck for Next Year", total_percantage)


