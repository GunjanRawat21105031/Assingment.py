#Question-1
load=input("Please enter a word/a sentence:")
load=load.lower().strip()
i=0
dict={}
if " " in load:
    load=str.split(load)
    while i<len(load):
        k=0
        count=0
        while k<len(load):
            if load[i]==load[k]:
                count+=1
                k+=1
            else:
                k+=1
        dict[f"{load[i]}"]=count
        i+=1
    for key,value in dict.items():
        print(f"{key}-{value}")
else:
    while i<len(load):
        k=0
        count=0
        while k<len(load):
            if load[i]==load[k]:
                count+=1
                k+=1
            else:k+=1
        dict[f"{load[i]}"]=count
        i+=1
    for key,value in dict.items():
        print(f"{key}-{value}")



#Question-2
date=int(input("Please enter date:"))
month=int(input("Please enter month:"))
year=int(input("Please enter year:"))

#Working with february
if month==2:
    if year%4==0:
        if date<29:
            new_date= date+1
            new_month=month
            new_year=year
        elif date==29:
            new_date=1
            new_month=month+1
            new_year=year
    else:
        if date<28:
            new_date=date+1
            new_month=month
            new_year=year
        elif date==28:
            date=1
            new_month=month+1
            new_year=year
#Working with 31 days months(except december)
elif month==1 or 3 or 5 or 7 or 8 or 10:
    if date<31:
        new_date=date+1
        new_month=month
        new_year=year
    elif date==31:
            new_date=1
            new_month=month+1
            new_year=year
#Working with 31 days months
elif month==4 or 6 or 9 or 11:
    if date<30:
        new_date=date+1
        new_month=month
        new_year=year
    elif date==30:
        new_date=1
        new_month=month+1
        new_year=year
#Working with last month of year
elif month==12:
    if date<31:
        new_date=date+1
        new_month=month
        new_year=year
    elif date==31:
        new_date=1
        new_month=month+1
        new_year=year+1
print(f"Next date:{new_date}/{new_month}/{new_year}")


#Question-3
list = [3, 9, 10]
final_list=[]
for number in list:
    number_square=number**2
    a_tuple=(number,number_square)
    final_list.append(a_tuple)
print(final_list)



#Question-4
grade=int(input("Please enter you grade points:"))

dict={10:{'letter_grade':'A+','performance':'Outstanding'},
           9:{'letter_grade':'A','performance':'Excellent'},
           8:{'letter_grade':'B+','performance':'Very Good'},
           7:{'letter_grade':'B','performance':'Good'},
           6:{'letter_grade':'C+','performance':'Average'},
           5:{'letter_grade':'C','performance':'Below Average'},
           4:{'letter_grade':'D','performance':'Poor'}}
if grade in range(4,11):
    for key in dict.keys():
        if key==grade:
            value=dict[key]
            print(f"Your Grade is {value['letter_grade']} and {value['performance']} Performance.") 
        else:
            continue
else:
    print('Error! Your grade is out of given range')



#Question-5

list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
rows=1
space=''
while rows<=6:
    for k in list:
        print(k, end='')
    list=list[:-2]
    rows+=1
    space+=' '
    print("")
    print(space,end='')



#Question-6
condition=True

#Defining dictionary to store the values
info={}
prompt="Y"
while condition:
    if prompt=="Y":
        SID=int(input("Please Enter SID of Student:"))
        name=input("Please enter the name of the Student:")
        info[SID]=name
        prompt= input("If you want to enter more details, Enter Y. Else, Enter N.")
        condition = True

    else:
        condition = False

#a)
for key,value in info.items():
    print(f"{key} is {value}")
print("")

#b)
Val_sort_dict= sorted(info.values())
print(f"Value sorted dictionary is {Val_sort_dict}")
print("")

#c)
Key_sort_dict= sorted(info.keys())
print(f"Keys sorted dictionary is {Key_sort_dict}")
print("")

#d)
SID_tbf=int(input("Please enter the student's SID whose detail you need- "))
if SID_tbf in info.keys():
    print(f"Name of the required student is {info[SID_tbf]}")
else:
    print("The SID is not present in the given Data")
print("")



#Question 7
number=int(input("Total elements of Fibonacci sequence that you want(must be greater than 1)- "))

#Entering first and second terms
a_1=1
a_2=0
n=0
#First Sum
sum=a_1+a_2

#intial terms
print(f"Fibonnaci sequence with {number} terms")
print(a_2)
print(a_1)

#Printing the fibonnaci terms
while n<number-2:
    a_n=a_2+a_1
    a_2=a_1
    a_1=a_n
    print(a_n)
    n=n+1
    sum+=a_n
average=sum/number

print("Average:",average)



#Question 8

set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}

#a)
notboth=set1^set2
print(f"Set with elements not common in both:{notboth}")

#b)
onlyinone=set1^set2^set3
print(f"Set of elements that is only in one of three:{onlyinone}")

#c)
onlyintwo=(set1|set2|set3)- (set1^set2^set3)-(set1&set2&set3)
print(f"Set of elements that is only in two sets at a time:{onlyintwo}")

#d)
new_set=set()
for n in range(1,11):
    new_set.add(n)
not_set1=new_set-set1
print(f"set of all integers in the range 1 to 10 that are not in Set1:{not_set1}")

#e)
new_set2=set()
for n in range(1,11):
    new_set2.add(n)
not_all3=new_set2 - (set1|set2|set3)
print(f"set of all integers in the range 1 to 10 that are not in Set1 and Set2 and Set3:{not_all3}")







