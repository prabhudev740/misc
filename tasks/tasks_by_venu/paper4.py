# 1. Sort the below list without using inbuilt function
# I = [2,3,-5,-7,9,4,6,-1,-8,0]
def sort(num, start, end):
    if start >= end:
        return 
    mid = (start + end) // 2
    left = sort(num, start, mid)
    right = sort(num, mid+1, end)
    
    merge(num, start, end, mid)
    
def merge(num, start, end, mid):
    s= start
    e = mid + 1
    res = []
    
    while s <= mid and e <= end:
        if num[s] < num[e]:
            res.append(num[s])
            s += 1
        else:
            res.append(num[e])
            e += 1
            
    if  s <= mid:
        res.extend(num[s:mid+1])
    if e <= end:
        res.extend(num[e:end+1])
        
#     print(res, num)
        
    for i, v in enumerate(res):
        num[i + start] = v
            

nums = [2,3,-5,-7,9,4,6,-1,-8,0]
sort(nums, 0, len(nums)-1)
print(nums)


# 2. Define a function which returns a list contains only the palindrome strings from the list
# of provided string elements
# input List of strings
# output: List of palindrome strings

def is_pallindrome(string):
    start = 0
    end = len(string) -1
    
    while start < end:
        if string[start] != string[end]:
            return False
        start +=1
        end -= 1
        
    return True

def filter_pallindromes(strs):
    res = []
    
    for string in strs:
        if is_pallindrome(string):
            res += [string]
        
            
    return res


strs = ['121', 'is', 'name', 'abba', 'defed']

print(filter_pallindromes(strs))


# 3 Define logic for identifying the even numbers and odd numbers from the given list and
# generate a dictionary as follows
# numbers = [4,5,7,2,9,8]
# result = {"even":[4,2,8],"odd":[5,7,9]}

def get_odd_even(numbers):
    res = {'even': [], 'odd': []}
    for num in numbers:
        if num % 2:
            res['odd'].append(num)
        else:
            res['even'].append(num)
            
    return res

numbers = [4,5,7,2,9,8]
print(get_odd_even(numbers))


# 4. Define a function which returns dictionary that stores the words and it's length from
# the given text
# text = "Be happy"
# Expected Output : {"Be":2,"happy":5}

def get_word_len(text):
    temp = ''
    count = 0
    res = {}
    
    for char in text:
        if char == " ":
            res[temp] = count
            count = 0
            temp = ''
            continue
        
        count += 1
        temp += char

    res[temp] = count
    return res
    
text = "Be happy"
print(get_word_len(text))


# 5. Let's consider there is a list which contains usernames, You have received
# requirement to add one more username to the list (without using append and
# assignment approaches)
# input : ["user1","user2"]
# output: ["user1","user2","user3"]

input1 = ["user1","user2"]
# input1.append('user3')
input1.extend(['user3'])
print(input1)

input1.insert(len(input1), 'user4')
print(input1)


# 6. Define the logic for generating the email id based on username and department
# Get the username and department as a input and create a email id from it
# input :
# username: msys
# department: automation
# output:
# msys.automation@gmail.com
# Note: Generated email id should contain @ and should end with .com

def genearate_email(uname, dept):
    return f"{uname}.{dept}@gmail.com"

username= 'msys'
department= 'automation'
print(genearate_email(username, department))


# 7. In the given string, remove the special characters and add a space instead of that
# "Msys&Technologies@Chennai*"
# 8. What is the return type of arbitrary positional arguments and arbitrary keyword
# arguments

def remove_special_chars(text):
    res = ""
    for char in text:
        if 'a' <= char.lower() <='z' or '0' <= char <= '9':
            res += char 
        else:
            res += ' '
            
    return res

print(remove_special_chars('Msys&Technologies@Chennai*'))


# 9. Given a string "abcde", Display the output as "a1b2c3d4e5"

def get_alnum(text):
    res = ''
    for index in range(len(text)):
        res += text[index] + str(index + 1)
        
    return res
text = 'abcde'

print(get_alnum(text))


# 10. Generate a dictionary from the two given lists using dict function (without using for
# loops) and calculate the sum of all the values in the dictionary using reduce and
# anonymous concepts
# L1 = ["a", "b"] L2 = [1,2]
# Expected Output:
# data = {"a":1, "b":2}
# sum = 3

L1= ["a", "b"] 
L2 = [1,2]

print(dict(map(lambda k, v: (k, v), L1, L2)))

# 11. Define Calculator logic in such a way that addition and subtraction functions should
# be in one python file and multiplication and division should be in another python file,
# Access these functions and utilize them inside the main file.

mul_div = """
def mul(num1, num2):
    return num1 * num2
    
def div(num1, num2):
    return num1 // num2
"""

sum_sub = """
def add(num1, num2):
    return num1 + num2
    
def sub(num1, num2):
    return num1 - num2
"""

with open('sum_sub.py', 'w') as fp:
    fp.write(sum_sub)

with open('mul_div.py', 'w') as fp:
    fp.write(mul_div)
    
from sum_sub import add, sub
from mul_div import div, mul

n1, n2, = 10, 5

print(add(n1,n2))
print(sub(n1, n2))
print(mul(n1, n2))
print(div(n1, n2))


# 12. Solve the following scenarios.
# Let's assume that there is a tuple containing username, You have got a
# requirement to add password also into it.
# O Input : ("user1")
# O Output: ("user1","password1")
# Below logic is failing with an error message, Instead of auto generated Error,
# Please display the user defined message saying "Error: Cannot concatenate
# String and Number".
# print("msys" + 2007)

# Scenario 1:
def add_password(uname, passwd):
    res = uname + (passwd, )
    return res

uname = ("user1", )
output = add_password(uname, 'password1')
print(output)

# Scenario 1:
class Error(Exception):
    pass

try:
    print("msys" + 2007)
except :
    raise Error('Cannot concatenate String and Number')


# 13. Let's assume there is function defined which expects only list as an argument,
# However there is chance that sometimes function will be called with different type of
# data, Now Fix this scenario to handle the other types without breaking the code.
# Scenario 1: If the argument provided is a list then, Print inside the function as
# "valid argument ".
# Scenario 2: if the argument provided is a different data type, then Print a
# message saying " invalid argument, You have provided data type (str/int) “
# ●

def is_valid_list(data):
    if isinstance(data, list):
        print("valid argument")
        return
        
    print('invalid argument, You have provided data type (str/int) ')
    
print(is_valid_list([1, 2, 3]))
print(is_valid_list(1))


# 15. Define logic for generating the random password with the provided length as an
# input

import random 

def generate_password(length):
    if not length:
        return ''
    return  random.choice(low + upcase + nums +special_char) + generate_password(length - 1)

low = 'abcdefghijklmnopqrstuvwxyz'
upcase = low.upper()
nums = '1234567890'
special_char = '@#$%^&*(){}[]+-_=\/'

for _ in range(20):
    print(generate_password(11))


# 16. Let's consider there are two files, one file contains testnames, other file contains
# testnames and status for each one. Generate dictionary with key's as testname and
# value as status
# Input :
    # File1.txt:
        # test1
        # test2
    # File2.txt:
        # test1-pass
        # test2-fail
# Output:
    # { "test1" : "pass", "test2" : "fail"}
    
    
file1_data = """test1
test2"""

file2_data = '''test1-pass
test2-fail'''

with open('file1.txt', 'w') as fp:
    fp.write(file1_data)
    
with open('file2.txt', 'w') as fp:
    fp.write(file2_data)
    
with open('file2.txt') as fp:
    data = dict(map(lambda test_data: test_data.replace('\n', '').split('-'), fp.readlines()))
    
print(data)


# 17. Define the function which returns the counts of saturdays part of a year (year is an
# input [Ex: 2022])

import datetime

def saturdays_count(year):
    count_saturday = 0
    date = datetime.date(year,1,1)
    while date.year == year:
        if date.weekday() == 5:
            count_saturday +=1
        date += datetime.timedelta(days=1)
    return f'Number of Saturdays in the {year} are {count_saturday}'
  

# year = int(input())
year = 2000
print(saturdays_count(year))


# 18. Write sample code for reproducing the below errors and print the user defined
# messages with the use of exception handling concept
# IndexError,
try:
    arr = []
    print(arr[0])
except IndexError:
    print('Wrong index passed')

# TypeError, 

def is_int(num):
    if not isinstance(num, int):
        raise TypeError('Num is not "int"')
    return True

print(is_int(10))
try:
    print(is_int(10.5))
except TypeError:
    print('Num is not a intiger')

# AttributeError, 
class Test:
    a = 10
    
test = Test()
print(test.a)

try:
    print(test.b)
except AttributeError:
    print('Attribute is not present')

# ValueError
try:
    int('a')
except ValueError:
    print("Value must be integers only")

# 19. Define a generator to print the numbers between o to n (including) which are
# divisible by 5 and should be even
# N = 20
# Output: 10 20

def give_nums(N):
    for num in range(N+1):
        if not num % 5 and not num % 2:
            yield num
            
for i in give_nums(20):
    print(i)


# 20. Define sample code to achieve the following OOPS concepts
# Inheritance
class Parent:
    p_data = 10
    
class Child(Parent): # Here we are inheriting Parent class to the child class
    c_data = 20
    
c_obj = Child()
print(c_obj.c_data, c_obj.p_data)


# ● Method Overriding
class Parent:
    def __init__(self):
        self.a = 100
    
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.b = 200
        
c_obj = Child()
print(c_obj.a, c_obj.b)
        
# ● Encapsulation
class Account:
    def __init__(self):
        self.__var = 10
        
    def get_var(self):
        print(self.__var)
        
paytm = Account()
paytm.get_var()
    
# Method overloading
def adder(*args, **kwargs):
    res = 0
    
    for num in args:
        res += num
    
    return res

print(adder(1, 2, 3, 4, 5))

# • Abstraction



# 21. Imagine a scenario where you are required to fetch the employee names who joined
# after 02 Sep 2022 and location is Hyderabad
# employee_ data = {
# "priya":{
# "location" : "Hyderabad"
# "joining_date": "05/09/2022"
# },
# "mahi": {
# "location" : "Bangalore"
# "joining_date":"20/02/2023"
# },
# "raja": {
# "location" : "Hyderabad"
# "joining_date": "14/10/2022"
# },
# "prabhu":{
# "location"  : "Bangalore"
# "joining_date": "02/01/2023"
# }
# }

def get_enames(e_data, given_date, loc):
    res = []
    joining_date = ()
    for name, data  in e_data.items():
        if loc == data['location']:
            joining_date =  tuple(map(int, data['joining_date'].split('/')))
#             if joining_date[2] < given_date[2] and joining_date[1] < given_date[1] and joining_date[0] < given_date[0]:
            if False not in map(lambda index: joining_date[2] < given_date[2], range(2, -1, -1)):
                continue
            res.append(name)
            
    return res


employee_data = {
"priya":{
"location" : "Hyderabad",
"joining_date": "05/09/2022"
},
"mahi": {
"location" : "Bangalore",
"joining_date":"20/02/2023"
},
"raja": {
"location" : "Hyderabad",
"joining_date": "14/10/2022"
},
"prabhu":{
"location"  : "Bangalore",
"joining_date": "02/01/2023"
}
}

given_date = tuple(map(int, '02/09/2022'.split('/')))
print(get_enames(employee_data, given_date, 'Hyderabad'))


# 22. Define the logic for verifying whether URL is Valid or Invalid
# Requirements for Valid URL.
# Should not contain any Special characters [,*,&,%,$,#,@,!] and Spaces
# ● Should start with https://
# Input: URLs will be stored inside a file, read the URLs from the input file [input.txt]
# Output: Generate a .txt file which contains the information whether URL is valid or
# not (URL, Status [valid/invalid])
# Example:
# Input :
# Input.txt [text file]
# https://m
# https://m
# Output:
# 1. https://m, valid
# 2. https://m, invalid
# Note: Define the logic with different approaches [1. Using RegEx 2. Without RegEx]


input_data = """https://m
https:// m"""

with open('input.txt', 'w') as fp:
    fp.write(input_data)
    
with open('input.txt') as fp:
    urls  = list(map(lambda line: line.strip('\n'), fp.readlines()))

def is_valid_url(url, protocol, special_char):
    if url[:len(protocol)] != protocol:
        return False
    
    for char in url[len(protocol):]:
        if char in special_char:
            return False
        
    return True
protocol = 'https://'
special_char = ' *&%$#@!'

with open('output.txt', 'w') as fp:
    for url in urls:
        if is_valid_url(url, protocol, special_char):
            fp.write(f"{url}, vaild\n")
        else:
            fp.write(f"{url}, invalid\n")
        


# 23. Write a logic for calculating the time taken for executing the python function

from datetime import datetime
import time

def adder(*args):
    res = 0
    
    for num in args:
        time.sleep(2)
        res += num
        
    return res


start = datetime.now().second
# print(adder(1))
print(adder(1, 2, 3, 4, 1, 2, 3, 4, 5, ))
end = datetime.now().second

print(end , start, end - start)


# 24. Define a logic for identifying the different files (In different format:.csv, .txt) which are
# part of a directory
# Input: You can create a directory and create the files with two different formats
# (Manually for the input)
# Output: Create two different directories and store this files separately based on
# the extension
# Example :
# Input:
# Assume file1.csv, file2.txt, file3.csv, file4.txt are present inside a directory
# (Any name)
# Output:
# CSV [Directory with the name CSV]
# file1.csv
# file3.csv
# TXT - [Directory with the name TXT]
# file4.txt
# file2.txt
              
import os
import shutil

csv_dir = "csv"
txt_dir = "txt"

# os.makedirs(csv_dir)
# os.makedirs(txt_dir)

shutil.move("D:/CODES/OJT_ASSIGNMENT/Programs/4_Fourth_paper/24_MyDir/manual/file1.csv","D:/CODES/OJT_ASSIGNMENT/Programs/4_Fourth_paper/24_MyDir/csv")
shutil.move("D:/CODES/OJT_ASSIGNMENT/Programs/4_Fourth_paper/24_MyDir/manual/file3.csv","D:/CODES/OJT_ASSIGNMENT/Programs/4_Fourth_paper/24_MyDir/csv")
shutil.move("D:/CODES/OJT_ASSIGNMENT/Programs/4_Fourth_paper/24_MyDir/manual/file2.txt","D:/CODES/OJT_ASSIGNMENT/Programs/4_Fourth_paper/24_MyDir/txt")
shutil.move("D:/CODES/OJT_ASSIGNMENT/Programs/4_Fourth_paper/24_MyDir/manual/file4.txt","D:/CODES/OJT_ASSIGNMENT/Programs/4_Fourth_paper/24_MyDir/txt")
# here we have to give file path which having CSV abd TXT files


                                           
# 25. Define a logic to print the combinations from the two the below input data
# Input :
# Output:
# [
# { 'Department': 'Bakkt', 'Team': 'Red'},
# { 'Department': 'Bakkt', 'Team': 'Yellow'}
# { 'Department': 'Bakkť', 'Team': 'Block'}
# { 'Department': 'Cisco', 'Team': 'Red'}
# { 'Department': 'Cisco', 'Team': 'Block'}
# { 'Department': 'Cisco', 'Team': 'Yellow'}]
input_data = {
'Department': ['Bakkt', 'Cisco'],
'Team' : ['Red', 'Yellow', 'Black']
}

output_data = []

for i in input_data['Department']:
    for j in input_data['Team']:
        output_data.append({'Department': i, 'Team': j})
        
print(output_data)


# 26. Print the pattern
# *1
# 21*
# *123
# Pattern for the input : 3
    
# Note: Logic should also work for dynamic input - Ex: 5
def generate(n):
    s, e = True, False
    
    for i in range(1, n + 1):
        if s:
            print('*', end ='')
            
        line = ''
        for j in range(1, i + 1):
            if s:
                line += str(j)
            if e:
                line = str(j) + line
        print(line, end = '')
        
        if e:
            print('*', end='')
            
        s, e = e, s
        print()
        
print(generate(5))
    

# 27. Write a python-selenium script to get the distance between Chennai and Bangalore
# using google-map



# 28. Define division logic which should also handle the the scenario if input argument
# (second argument) is 0, Use the decorator concept to include this validation before
# proceeding further on the actual functionality

def handle_diverror(func):
    def inner(num1, num2):
        if num2 == 0:
            return 0
        return func(num1, num2)
    return inner

@handle_diverror
def divide(num1, num2):
    return num1 // num2

print(divide(10, 0))


# 29. Find the element in a list using Binary Search Algorithm and return a tuple
# containing the element and its index.

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return target, mid
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return target, -1
                
            
arr = [1, 2, 3, 4, 5, 6]
print(binary_search(arr, 10))


# 30. Read data from json file [data.json] and generate an excel report with the provided
# data
# data.json
# {
# }
# Mahi
# Raj
# "company_name" : "MSYS"
# "employees":[
# Excel Sheet data should be displayed as shown below
# Company Name MSYS
# Name
# ]
# Employees
# {"name":"Mahi", "location":"Chennai" },
# {"name":"Raj", "location":"Bangalore" }
# Location
# Chennai
# Bangalore
import pandas as pd
import json
import openpyxl

with open('data.json', 'r') as f:      # Load the data from the JSON file
    data = json.load(f)

company_name = data['company_name']     # Extract the company name 
employee_data = data['employees']      # Extract the employee data
employees_df = pd.DataFrame(employee_data) # Create a Pandas DataFrame with the employee data

writer = pd.ExcelWriter('report.xlsx', engine='openpyxl')  # Create a new Pandas ExcelWriter object

employees_df.to_excel(writer, sheet_name='Employees', index=False) # Write the data to an Excel sheet

workbook = writer.book           # Get the workbook 
worksheet = writer.sheets['Employees']   # Get the worksheet objects

worksheet.write(0, 0, 'company_name')    # Add the company name to the worksheet
worksheet.write(0, 1, company_name)

worksheet.write(1, 0, 'Name')        # Add column headers to the worksheet
worksheet.write(1, 1, 'Location')


