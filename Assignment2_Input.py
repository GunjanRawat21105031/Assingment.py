#Question 1

#a)
input_string="python is a case sensitive language"
print("lenght of string=", len(input_string))

#b)
print("Reversed_string=", input_string[::-1])

#c)
print("new_string=", input_string[9:26])

#d)
#Trying the slicing way to form new string instead of replace 
new_string2= input_string[0:12]+"object oriented"+input_string[26:36]
print("new string=", new_string2)

#e)
print(input_string.index("a"))


#f)
input_string=input_string.replace(" ","")
print(input_string)


#Question 2

name=input("Enter your name:")
SID=int(input("Enter student ID:"))
dept_name=input("Enter department name:")
CGPA=float(input("Enter CGPA:"))

print('Hey, %s Here!'%(name))
print('My SID is %s'%(SID))
print('I am from %s department and my CGPA is %s' %(dept_name,CGPA))

#Question3

a=56
b=10

#a)
print("a & b=",a & b)

#b)
print("a | b =", a | b)

#c)
print("a ^ b =", a ^ b)

#d)
print("2 bit left shift of a=", a<<2)
print("2 bit left shift of a=", b<<2)

#e)
print("2 bit right shift of a=", a>>2)
print("4 bit left shift of b=", b>>4)


#Question4 

a = int(input("Enter 1st no. : "))
b = int(input("Enter 2nd no. : "))
c = int(input("Enter 3rd no. : "))

if a > b:
    if a > c:
        highest_number = a
    else:
        highest_number = c

if b > a:
    if b > c:
        highest_number = b
    else:
        highest_number = c

print(f"Highest no. = {highest_number}")



#Question 5

string=input("Enter any word")

if "name" in string:
    print("Yes")

else:
    print("No")

    
 #Question6

l1=int(input("Lenght of first side="))
l2=int(input("Lenght of second side="))
l3=int(input("Lenght of third side="))
print("Is triangle possible?")
if l1+l2>l3 and l2+l3>l1 and l3+l1>l2:
    print("Yes")
else:
    print("No")
