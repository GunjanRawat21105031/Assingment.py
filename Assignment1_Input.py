#Question-1

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
num3 = int(input("Enter third number"))
avg = (num1 + num2 + num3)/3 
print("Average=", avg)

#Question-2

a = float(input("Enter Gross Income"))
b = int(input("Enter number of dependents"))
c = a - 10000 - (3000*b)
print("Taxable Income=",c)

#Question-3

print("Student= [SID, Name, Gender, Course Name, CGPA]")
student= int(21105031), 'Gunjan' , 'F' , 'ECE' , float(9.8)
print(student)

#Question-4

#Maximum marks=100
M1 = int(input("Marks of student 1 : "))
M2 = int(input("Marks of student 2 : "))
M3 = int(input("Marks of student 3 : "))
M4 = int(input("Marks of student 4 : "))
M5 = int(input("Marks of student 5: "))
FinalMarks = [M1, M2, M3, M4, M5]
print("FinalMarks:",FinalMarks)

#Question-5

color=['Red','Green','White','Black','Pink','Yellow']
print(color)

#(A)
color.pop(3)
print("List_without_4thElement:", color)


#(B)
color[3:5]=['Purple']
print("List_Black,Pink->Purple:", color)
