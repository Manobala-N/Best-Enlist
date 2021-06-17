#1).Merging Two Dictionaries

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

#2).Removing a key from the Dictionary

D={'a': 100, 'b': 200, 'c': 300, 'd': 400}
print("Dictionary = " , D)

if 'a' in D: 
    del D['a']
print("Dictionary after deletion " , D)

#OUTPUT
#Dictionary =  {'a': 100, 'b': 200, 'c': 300, 'd': 400}
#Dictionary after deletion  {'b': 200, 'c': 300, 'd': 400}

#3).Mapping two lists into a dictionary

keys = ['Sachin', 'Dhoni', 'Raina' , 'kholi' , 'Rahul']
print("List1 Player Names : " , keys)

values = ['10','7', '3' , '18' , '1' ]
print("List2 Player Numbers : " , values)

New_Dict = dict(zip(keys, values))
print("Indian Cricketers Jersey Numbers : " , New_Dict)

#OUTPUT
#List1 Player Names :  ['Sachin', 'Dhoni', 'Raina', 'kholi', 'Rahul']
#List2 Player Numbers :  ['10', '7', '3', '18', '1']
#Indian Cricketers Jersey Numbers :  {'Sachin': '10', 'Dhoni': '7', 'Raina': '3', 'kholi': '18', 'Rahul': '1'}

#4).Finding the length of a set

CSK = {"Dhoni","Raina" ,"Bravo", "Jadeja", "SamCurran" , "D.Chahar" , "Du.Plesis"}
print("Set = " , CSK)

print("Length of the Set = " , len(CSK))

#OUTPUT
#Set =  {'Raina', 'Du.Plesis', 'D.Chahar', 'Bravo', 'Dhoni', 'Jadeja', 'SamCurran'}
#Length of the Set =  7

#5).Removing the intersection of a 2nd set from the 1st set
set1 = {10,20,30,40,50,60}
set2 = {40,50,60,70,80,90,100}
print("Original sets:")
print("Set 1 = " , set1)
print("Set 2 = " , set2)

set1-=set2
print("\nRemoving the intersection of a 2nd set from the 1st set")
print("Set 1 = " , set1)
print("Set 2 = " , set2)

#OUTPUT
#Original sets:
#Set 1 =  {40, 10, 50, 20, 60, 30}
#Set 2 =  {100, 70, 40, 80, 50, 90, 60}

#Removing the intersection of a 2nd set from the 1st set
#Set 1 =  {10, 20, 30}
#Set 2 =  {100, 70, 40, 80, 50, 90, 60}