#1).Creating Three variables with same values
a=b=c=10

print ("a = " , a , " \nb = " , b , "\nc = " , c)

a=a/10     # Dividing a by 10
print("After division a =" , a)

b=b*50     # Multiplying b by 50
print("After Multiplication b =" , b )

c=c+60     # Increasing c by 60
print("After addition c =" , c) 

#OUTPUT:
# a =  10  
# b =  10 
# c =  10
# After division a = 1.0
# After Multiplication b = 500
# After addition c = 70]

#2).Creating a string variable of 5 characters
String = "Rakul"
print (String)

new = list(String)           #Converting String to List
new[2] = "g"                 #Replacing 3rd character with "g"
print(''.join(new))          #Converting Lost to String

#OUTPUT
#Rakul
#Ragul

#3)Create two values (a,b) of int,float data type
a=25
b=25.0
print("Before Conversion :")
print("a = " , a ,"\nb = " ,b)

#converting a from int to float datatype & b from float to int datatype
a=float(a)
b=int(b)
print("After Conversion :")
print("a = " , a ,"\nb = " ,b)

#Ouput
# Before Conversion :
# a =  25 
# b =  25.0
# After Conversion :
# a =  25.0 
# b =  25

