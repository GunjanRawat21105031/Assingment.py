#Question1
def TowerofHanoi(n,source,auxillary,destination):
    if n==1:
        print("Move disc 1 from source",source,"to destination",destination)
        return
    TowerofHanoi(n-1,source,auxillary,destination)
    print("Move disc",n,"from source",source,"to destination",destination)
    TowerofHanoi(n-1,auxillary,destination,source)

TowerofHanoi(3,'A','B','C')

#Question2
n = int(input("Enter the number of rows in Pascal's Triangle: "))

#using recursions
print("Using recursions:")
def pascal(n, originaln=n):
    if n == 0:
        return
    
    pascal(n-1,originaln)
    print('  '*(originaln-n), end='')

    a=1
    for i in range(1, n+1):

        print(a, end ='   ')
        a = a * (n - i) // i
    print()
pascal(n)

#using loops
print("Using loops:")
for line in range(1, n+1):
    print('  '*(n - line), end='')

    x = 1
    for i in range(1, line+1):

        print(x, end='   ')

        x = x * (line - i) // i
    print()


# Question3
a = int(input("Enter the first number: "))
b = int(input("Enter the first number: "))

# ensuring that denominator is not zero
while b == 0:
    b = int(input("Denominator cannot be zero. Please enter a non zero number : "))

Q, R = divmod(a, b)
m = [Q, R]


def division():
    q, r = divmod(a, b)
    print(f"Questiont:{q}\nRemainder:{r}")

division()

#a)
print(callable(division))

#b)
if all(divmod(a, b)):
    print('All the values are non zero')
else:
    print('All the values are not non zero')

#c)
m.extend([4, 5, 6])
print("After adding 4,5,6 : ", m)
filtered = filter(lambda n: n > 4, m)
print("Values greater than 4 are : ", list(filtered))

#d)
s = set(m)
print(s)

#e)
f_s = frozenset(s)
print("Immutable set : ", f_s)

#f)
m = max(f_s)
print(hash(str(m)))

#Question-4
class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid
    
    def __del__(self):
        print("Object destroyed")

#assigning values
student1 = Student("Gunjan Rawat", 21105031)
print("Object created")

#printing the assigned values
print(f"The name of the student it {student1.name} and SID is {student1.sid}.")

#deleting object
del student1

#Question-5
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __del__(self):
        print(f"Employee {self.name} record deleted")

a = Employee("Mehak", 40000)
b = Employee("Ashok", 50000)
c = Employee("Viren", 60000)

#a)
a.salary = 70000
print(f"a. The updated salary of the employee {a.name} is {a.salary}")

#b)
print("b. ", end='')
del c

#Question-6
#George utters a word
word = input("Enter the first word: ")

#Barbie's word
testword = input("Enter a new meaningful word to test your friendship: ")


def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

#test 
if count_in_dict(word) != count_in_dict(testword):
    print("The letters aren't exact, friendship is fake!!")

#shopkeeper's input 
def userinput():
    ans = input("\nDoes the word makes sense?(y or n)\n")

    if ans == 'y':
        print("The friends pass the friendship test!!\n\n")
    elif ans == 'n':
        print("The word doesn't have a meaning, friendship is fake!!\n\n")
    else:
        print("Invalid input, try again")
        userinput()
userinput()
