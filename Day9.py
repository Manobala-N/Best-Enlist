#1). Program to loop through a list of numbers and add +2 to every value to
elements in list

List1=[1,2,3,4,5,6,7,8,9,10]
print("List of Numbers : " , List1)
List2=[]
for i in List1:
  i=i+2
  List2.append(i)

print ("Adding 2 to the List of Numbers :", List2)

#OUTPUT
#List of Numbers :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Adding 2 to the List of Numbers : [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#2). Program to get the given pattern

n = int(input('Enter number: ')) 
for i in range(n): 
	print(''.join(map(str,range(n-i,0,-1))))

#OUTPUT

#Enter number: 5
#54321
#4321
#321
#21
#1

#3).Fibonnaci Series

nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

#OUTPUT
#How many terms? 10
#Fibonacci sequence:
#0
#1
#1
#2
#3
#5
#8
#13
#21
#34

#4). Armstrong Number

num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#OUTPUT
#Enter a number: 153
#153 is an Armstrong number

#5). Multiplication table of 9

a=9
for i in range(1,11):
  c=a*i
  print(a,"*",i,"=",c)

#OUTPUT
#9 * 1 = 9
#9 * 2 = 18
#9 * 3 = 27
#9 * 4 = 36
#9 * 5 = 45
#9 * 6 = 54
#9 * 7 = 63
#9 * 8 = 72
#9 * 9 = 81
#9 * 10 = 90

#6).Positive or Negative

a=int(input("Enter the Number :"))
if(a>0):
  print(a ," is positive")
elif(a==0):
  print(a , " = 0")
else:
  print(a , " is Negative")

#OUTPUT
#Enter the Number :6
#6  is positive

#7). Converting the number of days to ages

days=int(input("Enter the Number of Days:"))
Age=days/365
print("Age of the Person : " , round(Age,1)," yrs")

#OUTPUT
#Enter the Number of Days:5400
#Age of the Person :  14.8  yrs

#8). Trignometric Functions

import math
  
a = math.pi/6
   
print ("The value of sine of pi/6 is : ", end="")
print (round(math.sin(a),2))
   
print ("The value of cosine of pi/6 is : ", end="")
print (round(math.cos(a),2))

#OUTPUT
#The value of sine of pi/6 is : 0.5
#The value of cosine of pi/6 is : 0.87

#9). Calculator

print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

ch=int(input("Enter Choice(1-4): "))

if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Sum = ",c)
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print("Product = ",c)
elif ch==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("Quotient = ",c)
else:
    print("Invalid Choice")

#OUTPUT
#Calculator
#1.Add
#2.Substract
#3.Multiply
#4.Divide
#Enter Choice(1-4): 3
#Enter A:25
#Enter B:4
#Product =  100