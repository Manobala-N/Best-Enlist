#1). Write a Python program for all the cases which can check a string contains only a certain set of
characters (in this case a-z, A-Z and 0-9).

import re

if __name__ == '__main__':
    string = "YourString123"
    pattern = re.compile("[A-Za-z0-9]+")

    # if found match (entire string matches pattern)
    if pattern.fullmatch(string) is not None:
        print("Found match: " + string)
    else:
        # if not found match
        print("No match")

#OUTPUT
#Found match: YourString123

#2). Write a Python program that matches a word containing &#39;ab&#39;.

import re
def text_match(text):
        patterns = '\w*ab.\w*'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("He is abnormal."))
print(text_match("Good evening."))

#OUTPUT
#Found a match!
#Not matched!

3).Write a Python program to check for a number at the end of a word/sentence.

import re
def end_num(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False

print(end_num('Hello'))
print(end_num('Task Day13'))

#OUTPUT
#False
#True

#4). Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string

import re
results = re.finditer(r"([0-9]{1,3})", "Search in Page numbers 34 1 585")
print("Number of length 1 to 3")
for n in results:
     print(n.group(0))

#OUTPUT
#34
#1
#585

#5). Write a Python program to match a string that contains only uppercase letters

import re
print(bool(re.match('^[A-Z]+$', 'BESTENLIST')))
print(bool(re.match('^[A-Z]+$', 'Bestenlist')))

#OUTPUT
#True
#False