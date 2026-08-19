# 1.
def greet_students(name, nChar):
    for i in range(nChar):
        print(name[i])

name = input("Enter a Name : ")
nChar = input("Enter any numeric number : ")
nChar = int(nChar)
greet_students(name, nChar)

'''
a. The code will output:

J
o
s
e
p

b. The code will throw an IndexError.
c. A try-except block may be added in order to abort the program and display a comprehensible error message if the user enters a number greater than the name's length.
'''

# 2.
'''
original snippet:

def greet_students(name, nChar):
    for i in range(nChar)
        print(name[0 : nChar])

name = input("Enter a Name")
greet_students(name, len(name))

a. The second line (line 26) lacks a colon at the end of the statement. The error was corrected upon adding the colon.
b. repaired snippet:
'''

def greet_students(name, nChar):
    for i in range(nChar, 0, -1):
        print(name[0 : i])

name = input("Enter a Name")
greet_students(name, len(name))

# 3.
def sum_of_squared(n):
    acc = 0
    for i in range(1, n + 1):
        acc += i ** 2
    return acc

n = 0
while n < 1 or n > 100:
    n = input("Enter a number from 1 to 100 : ")
    n = int(n)

print("Sum of all squared numbers is", sum_of_squared(n))