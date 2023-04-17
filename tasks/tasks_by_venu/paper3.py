# 1. Write a program in which two strings are given and determine if they share a 
# common substring. A substring may be as small as one character. The function 
# returns either “YES” or “NO”. 

def is_substr(mainstr, substr):
    substr_len = len(substr)
    mainstr_len = len(mainstr)

    for index in range(mainstr_len):
        if substr == mainstr[index:index+substr_len]:
            return True

    return False

is_substr("hello", 'help')


# 2. Write a decorator function that will record the number of times a function is 
# called. Your decorator function should be called record_calls and call_count 
# attribute that keeps track of the number of times it was called. 

def record_calls(func):
    def inner():
        global call_count
        call_count += 1
        func()
    return inner

@record_calls
def test_function():
    pass

call_count = 0

test_function()
test_function()
test_function()
test_function()
test_function()

print(call_count)


# 3. Write a function called interleave which accepts two iterables of any type and 
# returns a new iterable with each of the given items "interleaved" (item 0 from 
# iterable 1, then item 0 from iterable 2, then item 1 from iterable 1, and so on). An 
# assumption here that both iterables contain the same number of elements. 
def form_str(str1, str2):
    res = ""

    for item1, item2 in zip(str1, str2):
        res += item1+item2

    return res

def form_list(list1, list2):
    res = []

    for item1, item2 in zip(list1, list2):
        res.append(item1)
        res.append(item2)

    return res

def form_tuple(tuple1, tuple2):
    res = ()

    for item1, item2 in zip(tuple1, tuple2):
        res += (item1, item2)

    return res

# def form_set(set1, set2):
#     # set stores items randomly
#     res = set()

#     for item1, item2 in zip(set1, set2):
#         res.add(item1)
#         res.add(item2)

#     return res

def form_dict(dict1, dict2):
    res = {}

    for key1, key2 in zip(dict1, dict2):
        res[key1] = dict1[key1]
        res[key2] = dict2[key2]

    return res

def get_interleaved(iterable1, iterable2):
    res = None
    
    if isinstance(iterable1, str):
        res = form_str(iterable1, iterable2)
    if isinstance(iterable1, list):
        res = form_list(iterable1, iterable2)
    if isinstance(iterable1, tuple):
        res = form_tuple(iterable1, iterable2)
    # if isinstance(iterable1, set):
    #     res = form_set(iterable1, iterable2)
    if isinstance(iterable1, dict):
        res = form_dict(iterable1, iterable2)

    return res


print(get_interleaved("abc", 'xyz'))
print(get_interleaved([1, 2, 3], [5, 6, 7]))


# 4. Write to_celsius function that accepts a temperature in Fahrenheit as input and 
# returns a temperature in Celsius. 
def get_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

cel = float(input())
print(get_celsius(cel))


# 5. Write a function that accepts an iterable and returns a new iterable with all items 
# from the original iterable except for duplicates. 
# Ex. uniques_only([1, 2, 2, 1, 1, 3, 2, 1]) 
# [1, 2, 3] 

def uniques_only(collection):
    temp_type = type(collection)
    new_collection = type(collection)()
    is_str = isinstance(collection, str)

    for item in collection:
        if item not in new_collection:
            if is_str:
                new_collection += item
            else:
                new_collection += temp_type([item])
    
    return new_collection
    
uniques_only([1, 2, 3, 4, 1, 1, 2])
uniques_only((1, 2, 3, 4, 1, 1, 2))
# uniques_only("abccc")


# 6. Write a function to_percent which accepts a number representing a ratio and 
# returns a string representing the percentage representation of the number to one 
# decimal place. 

def to_percent(number):
    return f"percentge of {number} is {number:.1f}%"

print(to_percent(89))


# 7. Write a function that accepts two strings and returns True if the two strings are 
# anagrams of each other. 

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    dict_str1 = {}
    dict_str2 = {}

    for ch1, ch2 in zip(str1, str2):
        if ch1 not in str2 or ch2 not in str1:
            return False

        if ch1 in dict_str1:
            dict_str1[ch1] += 1
        else:
            dict_str1[ch1] = 1

        if ch2 in dict_str2:
            dict_str2[ch2] += 1
        else:
            dict_str2[ch2] = 1

    for key1, key2 in zip(dict_str1, dict_str2):
        if dict_str1[key1] != dict_str2[key2]:
            return False

    return True
    

is_anagram("abb", "abc")


# 8. Write Row class that accepts any keyword arguments given to it and stores these 
# arguments as attributes. 
# Ex. >>> row = Row(a=1, b=2) 
# >>> row.a 
# 1
# >>> row.b 
# 2

class Row:
    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
        

row = Row(a=1, b=2)
print(row.a)
print(row.b)

# 9. Create a function is_leap_year that accepts a year and returns True if (and only 
# if) the given year is a leap year. 

def is_leap_year(year):
    if not year % 100 and year % 400: 
        return False
    if year % 4:
        return False
    return True

print(is_leap_year(2100))
print(is_leap_year(1998))
print(is_leap_year(2102))
print(is_leap_year(1900))
print(is_leap_year(512))
print(is_leap_year(596))

# 10. Write a function combine_lists should take two lists and return a new list 
# containing all elements from both lists. 
def combine_lists(list1, list2):
    res = []
    
    for item in list1:
        res += [item]
        
    for item in list2:
        res += [item]
        
    return res

combine_lists([1, 2, 3], [4, 5, 6])

# 11. Write a function, last_lines, which returns lines in a given ASCII text file in 
# reverse order. 
# For example, given the following file, my_file.txt: 
# This is a file 
# This is line 2 
# And this is line 3 
# The last_lines function should work like this: 
# >>> for line in last_lines('my_file.txt'): 
# ... print(line, end='') 
# ... 
# And this is line 3 
# This is line 2 
# This is a file 

# createing file
txt = """This is a file 
This is line 2 
And this is line 3 """

with open('my_file.txt', 'w') as fp:
    fp.write(txt)
    
# reverse function
    
def reverse(lines):
    start = 0
    end = len(lines) - 1
    
    while start < end:
        lines[start], lines[end] = lines[end], lines[start]
        start += 1
        end -= 1
    
# last_lines function
def last_lines(file_name):
    with open(file_name) as fp:
        lines = fp.read().split('\n')
        
    reverse(lines)
    return lines

for line in last_lines('my_file.txt'):
    print(line)


# 12. Write a function called parse_ranges, which accepts a string containing ranges of 
# numbers and returns an iterable of those numbers. 
# Ex: >>> parse_ranges('1-2,4-4,8-13') 
# [1, 2, 4, 8, 9, 10, 11, 12, 13] 

def get_range(ith_range):
    res = ith_range.split('-')
    return int(res[0]), int(res[1])

def add_nums(nums, r_start, r_end):
    for num in range(r_start, r_end+1):
        nums.append(num)

def parse_ranges(ranges):
    res = []
    
    ranges_list = ranges.split(',')
    
    for ith_range in ranges_list:
        start_range, end_range = get_range(ith_range)
        add_nums(res, start_range, end_range)
        
    return res

parse_ranges('1-2,4-4,8-13')


# 13. Write a function that accepts a string containing lines of numbers and returns a 
# list of lists of numbers. 
# Ex. matrix_from_string("3 4 5") 
# [[3.0, 4.0, 5.0]] 

def get_num_list(nums):
    res = [[]]
    
    for num in nums.split():
        res[0].append(float(num))
        
    return res

get_num_list("3 4 5")



# 14. Write a command-line program which helps a traveler keep track of the 
# restaurants they've visited in different cities and what they thought of each. The 
# program will accept two CSV files of restaurants, a "primary list" CSV and a 
# "sublist" one, and update the primary one with new restaurants from the trip one. 
import json

def display_json(file1):
    with open(file1) as f:
        data = json.load(f)
        print(data)

print(display_json('file1.json'))


# 15. Write a function get_hypotenuse that returns the hypotenuse of a right triangle 
# given the other two sides. 
# >>> get_hypotenuse(0, 0) 
# 0.0>>> get_hypotenuse(3, 4) 
# 5.0

from math import sqrt

def get_hypotenuse(height, base):    
    res = sqrt(height ** 2 + base ** 2)
    
    return res

print(get_hypotenuse(3, 4))
print(get_hypotenuse(0, 0))


# 16. Write a function split_in_half that splits a list in half and returns both halves. 
# >>> split_in_half([1, 2, 3, 4]) 
# ([1, 2], [3, 4]) 

def split_in_half(given_list):
    half = len(given_list) // 2
    
    return given_list[:half], given_list[half:]

split_in_half([1, 2, 3, 4])


# 17. Write a function that takes a sequence (like a list, string, or tuple) and a number n 
# and returns the last n elements from the given sequence, as a list. For example: 
# >>> tail([1, 2, 3, 4, 5], 3) 
# [3, 4, 5] 

def trail(seq, n):
    return seq[len(seq)- n:]

trail([1, 2, 3, 4, 5], 3)
trail("prabhu", 2)
trail((1, 2, 3, 4, 5), 1)


# 18. Create your own exception. 

class NumericError(Exception):
    pass

def is_valid_uname(name):
    if name.isnumeric():
        raise NumericError("Name cant't be alphanumeric")
        
    return True

is_valid_uname('Prabhu7')
is_valid_uname('7')


# 19. Write a function that takes two strings representing dates and returns the string 
# that represents the earliest point in time ? Ex. get_earliest("01/27/1832", 
# "01/27/1756") return '01/27/1756'. 

def get_earliest(date1, date2):
    date_ls1 = tuple(map(int, date1.split('/')))
    date_ls2 = tuple(map(int, date2.split('/')))
    
    if date_ls1[2] != date_ls2[2]:
        return date2 if date_ls1[2] > date_ls2[2] else date1
    elif date_ls1[1] != date_ls2[1]:
        return date2 if date_ls1[1] > date_ls2[1] else date1
    else:
        return date2 if date_ls1[0] > date_ls2[0] else date1
        
    
print(get_earliest("01/27/1832", "01/27/1756"))


# 20. Create a function that determines which day of the month the San Diego Python 
# meetup should be. It should accept year and month arguments and should return 
# a datetime.date object representing the day of the month for the meetup. 
# >>> meetup_date(2012, 3) 
# datetime.date(2012, 3, 22) 
import datetime

def meetup_date(year, month):      
    first_day = datetime.date(year, month, 1)       # We first calculate the date for the 1st day of the month
    
    first_day_weekday = first_day.weekday()         # here finding the day of the week for the 1st day of the month
    
    meetup_day = 26 - (first_day_weekday + 1) if first_day_weekday <= 3 else 32 - (first_day_weekday + 1)  # We calculate the number of days to the 4th Thursday of the month
   
    return f'{datetime.date(year, month, meetup_day)}, Meet up Date is {meetup_day}'     # here creating the datetime.date object and returning it 


year = int(input("Enter the Year: "))
month = int(input("Enter the month: "))
print(meetup_date(year,month))


# 21. Write a callable called float_range that acts sort of like the built-in range callable 
# but it should allow for floating point numbers to be specified as start, stop, and 
# step values. 
# >>> r = float_range(0.5, 2.5, 0.5) 
# >>> r 
# float_range(0.5, 2.5, 0.5) 
# >>> list(r) 
# [0.5, 1.0, 1.5, 2.0] 
# >>> len(r) 
# 4
# >>> for n in r: 
# ... print(n) 
# ... 
# 0.5 
# 1.0 
# 1.5 
# 2.0

def float_range(start, end, step):
    res = []
    while start < end:
        res.append(start)
        start += step
        
    return res

r = float_range(0.5, 2.5, 0.5)
print(r)
print(len(r))
    

#22. Write a function is_iterator so that it accepts an iterable and returns True if the 
# given iterable is an iterator. 
# is_iterator(iter([])) 
# True 
# >>> is_iterator([1, 2]) 
# False 

x = [1, 2, 3, 4]

z = iter(x)

def is_iterator(iterable):
    try:
        next(iterable)
        return True
    except TypeError:
        return False
    
print(is_iterator(x))
print(is_iterator(z))


# 23. Create a context manager. Context managers use a with block to bookend a 
# block of code with automatic setup and tear down steps.Your context manager, 
# suppress, should suppress exceptions of a given type: 
# >>> with suppress(NameError): 
# ... print("Hi!") 
# ... print("It's nice to meet you,", name) 
# ... print("Goodbye!") 
# ... 
# Hi! 
# But exceptions of other types shouldn't be suppressed (we're suppressing a 
# TypeError and a NameError is raised): 
# >>> with suppress(TypeError): 
# ... print("Hi!") 
# ... print("It's nice to meet you,", name) 
# ... print("Goodbye!") 
# ... 
# Hi! 
# Traceback (most recent call last): 
# File "<stdin>", line 3, in <module> 
# NameError: name 'name' is not defined

# from contextlib import suppress
class suppress:
    def __init__(self, error):
        self.error = error
        
    def __enter__(self):
        pass
        

    def __exit__(self, exc_type, exc_val, tb):
        print(exc_type, exc_val, tb)
        if exc_type == self.error:
            return True
        

with suppress(NameError):
    print("Hi!") 
    print("It's nice to meet you,", name) 
    print("Goodbye!") 
    
with suppress(TypeError):
    print("Hi!") 
    print("It's nice to meet you,", name) 
    print("Goodbye!") 


# 24. Write a class that represents a circle.The circle should have a radius, a diameter, 
# and an area. It should also have a nice string representation. 

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = self.get_diameter()
        self.area = self.get_area()
        
    def get_diameter(self):
        return 2 * self.radius

    def get_area(self):
        return 2 * 3.14 * self.radius**2
    
    def __str__(self):
        return f"""radius of circle = {self.radius}
        diameter = {self.diameter}
        area = {self.area}"""
    

c = Circle(5)
print(c)


# 25. Write a program to convert integers to Roman numbers. 
def get_romon(num, ints):
    if not num:
        return ''
    
    for i in reversed(ints):
        if i <= num:
            num = num - i
            return romons[i] + get_romon(num, ints)

romons = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 
          40: 'IL', 50: 'L', 90: 'IC', 100: 'C', 400: 'ID', 500: 'D', 900: 'IM', 1000: 'M'}
num = 1
# num = 11
# num = 9
# num = 51
num = 1002
num = 2345

print(get_romon(num, romons.keys()))



# 26. Write a function so that it accepts an iterable and returns True if the given iterable 
# is an iterator. 

x = [1, 2, 3, 4]
z = iter(x)

def is_iterator(iterable):
    try:
        next(iterable)
        return True
    except TypeError:
        return False
    
print(is_iterator(x))
print(is_iterator(z))


# 27. Write a class that represents a bank account, do bank operations. 


class HDFC:
    __acc_no_rec = 100000
    branch_name = 'BTM Layout'
    bank_name = 'HDFC Bank'
    ifsc = 'HDFC0001'
    
    def __init__(self, fname, lname, age, city, deposite):
        self.__account_no = self.__get_account_no()
        self.fname = fname
        self.lname = lname
        self.age = age
        self.city = city
        self.amount = deposite
        
    def __get_account_no(cls):
        cls.__acc_no_rec += 1
        return cls.__acc_no_rec
    
    def __str__(self):
        return f""" ======= Customer Details =======       
        account_no: {self.__account_no}
        name: {self.fname} {self.lname}
        age: {self.age}
        city: {self.city}
        deposite: {self.amount}
        """
    
    def display_amount(self):
        print(f"Account bal is {self.amount}")
        print()
        
    def deposite(self, bal):
        self.amount += bal
        print("Amount Deposited Successfully")
        print()
        
    def withdraw(self, bal):
        self.amount += bal
        print("Amount Withdrawn Successfully")
        print()
    
        

# a = HDFC('Prabhu', 'Panda', 23, "BBSR", 5000)
# print(a)
# b = HDFC('Prabhu', 'Panda', 23, "BBSR", 5000)
# print(b)
cust = HDFC('Prabhu', 'Panda', 23, "BBSR", 5000)
print(cust)
cust.display_amount()
cust.deposite(1000)
print(cust)
cust.display_amount()
cust.withdraw(2000)
print(cust)
cust.display_amount()


# 28. Standardize mobile numbers when given N mobile numbers. Sort them in 
# ascending order. Print them in the standard format. 

def standardize(mob_nums):
    n = len(mob_nums)

    for passes in range(n - 1, 0, -1):
        for i in range(passes):
            if mob_nums[i] > mob_nums[i + 1]:
                mob_nums[i], mob_nums[i + 1] = mob_nums[i + 1], mob_nums[i]
    
mob_nums = [766865, 769865, 767865, 764865, 762865, 761865]
standardize(mob_nums)
print(mob_nums)


# 29. Write a function called interleave which accepts two iterables of any type and 
# returns a new iterable with each of the given items "interleaved" (item 0 from 
# iterable 1, then item 0 from iterable 2, then item 1 from iterable 1, and so on). 

def interleave(iterable1, iterable2):
    res_type = type(iterable1)
    res = []
    
    iter1 = iter2 = 0
    
    while iter1 < len(iterable1) and iter2 < len(iterable2):
        res += [iterable1[iter1]]
        iter1 += 1
        res +=[(iterable2[iter2])]
        iter2 += 1
        
    if iter1 < len(iterable1):
        res += iterable1[iter1:]
    if iter2 < len(iterable2):
        print(res, iterable2[iter2:])
        res += iterable2[iter2:]
        print(res)
        
    if isinstance(iterable1, str):
        return ''.join(res)
    
    if isinstance(iterable1, tuple):
        return tuple(res)
    
    return res

print(interleave('123', 'abcde'))
print(interleave([1,2,3], [4, 5, 6]))
print(interleave((10,20,30), (40, 50, 60)))


# 30. Convert each list element to a key-value pair. 
# ex: 
# Input : test_list = [2323, 82, 129388, 95] 
# Output : {23: 23, 8: 2, 129: 388, 9: 5}


def get_half(num, x=1):
    while num // 10 ** x:
        x += 1 
    return x // 2

    
def get_dict(nums):
    res = {}
    
    for num in nums:
        half = get_half(num)
        res[num // 10 ** half] = num % 10 ** half
    return res
    

test_list = [2323, 82, 129388, 95] 
get_dict(test_list)