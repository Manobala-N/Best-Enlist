#1). lambda function that multiplies argument x with argument y

Mul = lambda x,y : x*y
print(Mul(5,6))

#OUTPUT
#30

#2).Fibonacci Series Using Lambda

from functools import reduce
fib_Series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
print(fib_Series(10))

#OUTPUT
#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#3).Multiplying each number of given list by a given  number 

list1 = [1,2,3,4,5]
n = 5
print("Original list: ", list1)
print("Given number: ", n)
list2=list(map(lambda number:number*n,list1))
print("Result:")
print(' '.join(map(str,list2)))

#OUTPUT
#Original list:  [1, 2, 3, 4, 5]
#Given number:  5
#Result:
#5 10 15 20 25

#4). Numbers divisible by 9

list3 = [10,14,18,24,27,32,36,40,45]

result = list(filter(lambda x: (x % 9 == 0), list3))

print("Numbers divisible by 9 are",result)

#OUTPUT
#Numbers divisible by 9 are [18, 27, 36, 45]

#5).No.of even numbers in List

list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original arrays:" , list4)
No_of_Even_Numbers = len(list(filter(lambda x: (x%2 == 0) , list4)))
print("Number of even numbers in the List: ",No_of_Even_Numbers

#OUTPUT
#Original arrays: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Number of even numbers in the List:  5
