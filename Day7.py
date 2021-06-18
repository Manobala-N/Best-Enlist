#1). Creating a function getting two integer inputs from user

def my_task(a,b):
   print("Addition of two numbers is " , (a+b))                        #Adding two numbers
   print("Subraction of two numbers is " , (a-b))                      #Subracting two numbers
   print("Division of two numbers is " , (a/b))                        #Dividing two numbers
   print("Multiplication of two numbers is " , (a*b))                  #Multiplying two numbers

my_task(10,5)                                                          #Calling Function

#OUTPUT
#Addition of two numbers is  15
#Subraction of two numbers is  5
#Division of two numbers is  2.0
#Multiplication of two numbers is  50

#2). Create a function covid( )

def covid(Patient_name,Body_Temperature=98):
   print("Patient Name is : " , Patient_name)
   print(Patient_name,"\b's Body Temperature is :",Body_Temperature) 

covid("Ram")
covid("Raghu" , 97.5)

#OUTPUT
#Patient Name is :  Ram
#Ram's Body Temperature is : 98
#Patient Name is :  Raghu
#Raghu's Body Temperature is : 97.5
