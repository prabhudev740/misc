# Questions
# 1. What are the differences between list and tuple? Which is faster and why? 
# 2. What is the lambda function in python? Explain with examples.
# 3. What is monkey patching and what is the use of monkey patch?

# 4. Write a python program to right rotate a List by n Enter position to rotate list item: 3 
# Sample input: [10, 20, 30, 40, 50, 60, 70] 
# Expected output: [50, 60, 70, 10, 20, 30, 40]

# 5. Write a program to reverse a number without using any inbuit function.
# 6. Given a list of first 10 natural numbers, write a program to find the square of all even numbers 
# and cube of all odd numbers and store them in another list




# Solution 1
# ---------------

# list and tuple both are ordered collection datatypes and both can store hetrogeinus datatypes

# list : Values are separated by comma and stored inside '[]'
#            Example: [1, 2, 3], [0, True, "abc"], [[0.5, False], "abc"], [1], etc
    
#        These are mutable. i.e. we can modify them after initialize.
#            Operation: append, pop, insert, extend, remove, etc
#        Used for storing data which can be modified later or we can add or remove data from collection.

#        Default value -> []
#        Represented as -> 'list'


# tuple : Values are separated by comma and stored inside '()'
#            Example: (1, 2, 3), (0, True, "abc"), ([0.5, False], "abc"), (1, ), etc
    
#         These are immutable. i.e. we can't modify them after initialize.
#         Used for storing data which later can't be modified, like- points, time, etc

#         Default value -> ()
#         Represented as -> 'tuple'


# Here tuple is more faster because it is immutable datatype which is more optimised by interpreter.



# Solution 2
# -------------

# These are the annonyus functions
# these will declared with 'lambda' keywords.
# Syntax:- lambda args: statement

# Ex: get_square = lambda a: a * a

# Best place to use these in function which takes or return a function. like map() and filter(), etc.
# suppose we want to take a list of number and from that we have get another list with bool value
# i.e. result list will store True if val is even or False if val is odd.

# arr = [1, 2, 3, 4, 5]
# res = list(map(lambda a: a % 2 == 0, arr))

arr = [1, 2, 3, 4, 5]
res = list(map(lambda a: a % 2 == 0, arr))
print(res)



# Solution 3
# -------------

class Bank:
    def __init__(self, bal):
        self.account_bal = bal

    def display(self):
        print(f"account bal is: {self.account_bal} rs")

cust1 = Bank(5000)
# cust1.display() # this will print the account bal and some reson we want to exeute a dummy func

def dummy_display(arg):
    print("This is dummy bal: 0 rs")

Bank.display = dummy_display  # monkey patching
cust1.display()



# Solution 4
# -------------
x = [10, 20, 30, 40, 50, 60, 70]
i = 3

#* ==== method 1 ====
res = []

for j in x[i+1:]:
    res.append(j)
res.extend(x[:i+1])

print(res)


#* ==== method 2 ====
res = x[i+1:] + x[:i+1]
print(res)


#* ==== method 3 ====
from collections import deque

l = deque(x)
l.rotate(-i-1)
print(list(l))


# Solution 5
# -------------

num = int(input("Enter a number"))
res = 0

while num:
    res = res * 10 + num % 10
    num //= 10

print("reveresed number", res)

# Solution 6
# -------------

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = []

for num in arr:
    if num % 2:
        res.append(num ** 3)
    else:
        res.append(num ** 2)

print("original list", arr)
print("result list", res)