# 11. Rewrite the program to get proper output 
# Match = 'version' 
# input=8 
# print(Match+input) 
# 12. How is memory management done in python? 
# 13. Give a real time example for multithreading. Is it a good idea to use multi-thread to 
# speed your Python code? 
# 14. When do you use generators in python? Give an example 
# 15. Give the scenarios, when you will get ‘ValueError’ 
# 16. Write a program to multiply two given number without using “*” operation and any in built 
# function

# Solution 11
# ------------
match = "version"
input = 8
# print(match + input)  # we will gat type error, because we are tying to concatinate 'str' with 'int'ArithmeticError

# To fix this we can typecast 'input' to 'str' using 'str()' 
print(match + str(input))

# Solution 12  --> memory management in python
# --------------
# Memory management in python done by combination of ref count and inbuilt garbage collector.

# ref_count keeps track of no of references to the object 
# once the ref_count become 0, garbage collector will free the memory

# garbage collecter runs cyclic way. once it found the ref_count 0 for an object
# it willwill automatically clear the object  and from memory.

# Solution 13
# ------------
import threading
import time

def adder(val, no_of_times):
    print("started adding")
    result = 0

    for iteration in range(no_of_times):
        result += val
        print(iteration, result)
        time.sleep(0.2)

    print(result)

def display(name, no_of_times):
    for iteration in range(no_of_times):
        print(iteration, name)
        time.sleep(0.1)


thread1 = threading.Thread(target=adder, args=(50, 10))
thread1.start()

thread2 = threading.Thread(target=display, args=("Prabh", 10))
thread2.start()

print("program finished")


# It may not be a good idea beacuse of GIL (Global Interpreter Lock)


# Solution 14
# ------------
# generators can be used for iteration purpose.
# The basic difference between generators and iterators is memory usage.
# iterator stores the data, while generators doesn't store the data

# Inbuit generators
nums = (i for i in range(1, 11))

print(nums)
print(list(nums))


# User defined generators using yeild keyword
# generator of even nums between 10 to 100

def get_evens(start, end):
    for num in range(start, end+1):
        if not num % 2:
            yield num

# here we are not returning the function
# yield will return the value and remeber the position of iteration.

evens = get_evens(10, 100)
print(evens)
print(list(evens))


# Solution 15
# -------------
# When we try to pass a argument wrong datatype inside a functon, we will get ValueError
# Example 1
# ------------
try:
    int("abc")
except ValueError:
    print("we are getting value error")

# Example 2
# ------------
def doubler(num):
    if not num.isnumeric():
        raise ValueError("Please enter a numeric value")
    return int(num) * 2

num = input()
try:
    print("doubled value is:", doubler(num))
except ValueError:
    print("the value entered is not numeric")

# Solution 16
# -----------
def multiply_nums(num1, num2):
    result = 0

    for count in range(num1):
        result += num2

    return result

result = multiply_nums(5, 3)
print(result)