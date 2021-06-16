#1).Creating a List
list1 = [1,2,3,4,5,6,7,8,9,10]
print ("list = " , list1)
list1.append(11)                                  #Appending a value
print ("list = " , list1)
list2 = [12,13,14,15]
list1.extend(list2)                               #Adding another items from list
print ("list = " , list1)
list1.insert(0,0)                                 #Appending value at a particular index
print ("list = " , list1)                         

del list1[0]                                      #Deleting a value
print ("list = " , list1)
Popped_Number = list1.pop()                       #Deleting using Pop function
print ("list = " , list1)
print ("Popped_Number =" , Popped_Number)

Smallest_Number = min(list1)                      #Identifying minimum value
print ("Smallest_Number = " , Smallest_Number)
Largest_Number = max(list1)                       #Identifying maximum value
print ("Largest_Number = " , Largest_Number) 

#OUTPUT
#list =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#list =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#list =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#list =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#list =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#list =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#Popped_Number = 15
#Smallest_Number =  1
#Largest_Number =  14


#2).Creating a Tuple and Reversing it

tuples = (1,'two',3,'four',5,'six',7,'eight',9,'ten')     #Creating a Tuple
print ("Tuple :")
print(tuples)
Reversed_Tuple = reversed(tuples)                         #Reversing the Tuple
print ("Reversed_Tuple :" ) 
print (tuple(Reversed_Tuple))

#OUTPUT
#Tuple :
#(1, 'two', 3, 'four', 5, 'six', 7, 'eight', 9, 'ten')
#Reversed_Tuple :
#('ten', 9, 'eight', 7, 'six', 5, 'four', 3, 'two', 1)

#3).Converting Tuple to List

aTuple = (1,'two',3,'four',5,'six',7,'eight',9,'ten');           #Creating a Tuple
print("Tuple = " , aTuple)
aList = list(aTuple)                                             #Converting Tuple to List
print ("List = ", aList)

#OUTPUT
#Tuple =  (1, 'two', 3, 'four', 5, 'six', 7, 'eight', 9, 'ten')
#List =  [1, 'two', 3, 'four', 5, 'six', 7, 'eight', 9, 'ten']



























