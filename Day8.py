#1). Merging Two Dictionaries

d1 = {'a': 100, 'b': 200}
print ("Dictionary 1 = " , d1)

d2 = {'c': 300, 'd': 400}
print ("Dictionary 2 = " , d2)

d = d1.copy()
d.update(d2)
print("Combined Dictionary = " , d)

#OUTPUT
#Dictionary 1 =  {'a': 100, 'b': 200}
#Dictionary 2 =  {'c': 300, 'd': 400}
#Combined Dictionary =  {'a': 100, 'b': 200, 'c': 300, 'd': 400}

#2). Sorting in Descending and Converting List to Set

numbers = [1, 3, 4, 2,7,9,5,10,8,6]
print("List =" , numbers)
numbers.sort(reverse = True)
print("Sorted List =",numbers)
set1=set(numbers)
print("Converted Set =" , set1)

#OUTPUT
#List = [1, 3, 4, 2, 7, 9, 5, 10, 8, 6]
#Sorted List = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#Converted Set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#3). Sorting Dictionary

test_dict = {'gfg': [7, 6, 3], 
             'is': [2, 10, 3], 
             'best': [19, 4]}
  
print("The original dictionary is : " + str(test_dict))
  
res = {key : sorted(test_dict[key]) for key in sorted(test_dict)}
  
print("The sorted dictionary : " + str(res))

#OUTPUT
#The original dictionary is : {'m': [7, 6, 3], 'w': [2, 10, 3], 'c': [19, 4]}
#The sorted dictionary : {'c': [4, 19], 'm': [3, 6, 7], 'w': [2, 3, 10]}

#4).Changing Certain Index with specific Value 

String1=input("Enter the String : ")
n=int(input("Enter the index to be replaced : "))
String2=String1.replace(String1[n],"X")
print("After Replacing : " , String2)

#OUTPUT
#Enter the String : Best Enlist
#Enter the index to be replaced : 5
#After Replacing :  Best Xnlist

#5). Changing Case of First letter of the String

String1=input("Enter the String : ")
n=int(input("Enter the index to be replaced : "))
String2=String1.replace(String1[n],"X")
print("After Replacing : " , String2)

#OUTPUT
#The original string is : best enlist
#The string after uppercasing initial character : Best enlist

#6). Finding the repeated items of a list

from collections import Counter
 
l1 = [1,2,3,3,4,5,6,6,7,8,9,9,9]
d = Counter(l1)
print(d)
 
new_list = list([item for item in d if d[item]>1])
print("Repeated Items in the list : " , new_list)

#OUTPUT
#Counter({9: 3, 3: 2, 6: 2, 1: 1, 2: 1, 4: 1, 5: 1, 7: 1, 8: 1})
#Repeated Items in the list :  [3, 6, 9]


#7). Checking the sum of three elements and dividing by a value which is given as an input by the user

a,b,c=2762,3482,9275
Sum1 = a+b+c
print("The Sum of Three Numbers is :" ,Sum1)

Divisor=int((input("Enter the divisor : ")))
d= Sum1 / Divisor

print("After divison : " , d )

#OUTPUT
#The Sum of Three Numbers is : 15519
#Enter the divisor : 47
#After divison :  330.1914893617021

#8). Finding the Mean,median,mode among three given numbers

import statistics
list1 = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    number = int(input())
  
    list1.append(number) # adding the element
          
print("The three Numbers is :", list1)

print("Mean of three numbers is : " , statistics.mean(list1))
print("Median of three numbers is : " , statistics.median(list1))
print("Mode of three numbers is : " , statistics.mode(list1))

#OUTPUT
#Enter number of elements : 3
#100
#100
#400
#The three Numbers is : [100, 100, 400]
#Mean of three numbers is :  200
#Median of three numbers is :  100
#Mode of three numbers is :  100


#9). Swapping cases of a given string

Original_string = input("Enter The String : ")
  
print("After Swapping All the Cases : " , Original_string.swapcase())

#OUTPUT
#Enter The String : Best Enlist
#After Swapping All the Cases :  bEST eNLIST

#10). Converting an integer to binary & octa decimal

Integer_Value=int(input("Enter the value of the Integer : "))
print("Equivalen Binary Value = ", bin(Integer_Value))
print("Equivalen Octa Decimal Value = ", oct(Integer_Value))

#OUTPUT
#Enter the value of the Integer : 344
#Equivalen Binary Value =  0b101011000
#Equivalen Octa Decimal Value =  0o530