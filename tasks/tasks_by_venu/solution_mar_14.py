# 21. You are given a string and width. Your task is to wrap the string into paragraph of width in 
# reverse order. Blank spaces should be ignored.
# for eg: i/p - first line contains a string with blank spaces - Hello, welcome to this 
# organisation.
#  the second line conatins the width - 4
#  o/p
# lleH
# ew,o
# mocl
# tote
# osih
# nagr
# tasi
# .noi

def get_wrapped(sentence, width):
    count = 0
    word = ""

    for char in sentence:
        if char == " ":
            continue

        word = char + word
        count += 1

        if not count % width:
            print(word)
            word = ''


sentence = "Hello, welcome to this organisation."
n = 4
get_wrapped(sentence, n)


# 22. Find the palindrome words with the count value from the given string.Output should be in 
# form of dict. key will be palidrome word and value will be number of occurence.
# i/p given a string - Nittin & his mom went to a park last friday. His Mom observed that the weather
# was too cool. Nittin also met his sis. If we reverse the number 1331 then we also get 1331. 
# o/p - {'nittin': 2, 'mom': 2, 'sis': 1, '1331': 2}

def is_pallindrome(word):
    if len(word) < 3:
        return False

    start_i = 0
    end_i = len(word) - 1

    while start_i < end_i:
        if word[start_i] != word[end_i]:
            return False
        start_i, end_i = start_i + 1, end_i - 1
    
    return True

def word_counter(target_dict, word):
    if word in target_dict:
        target_dict[word] += 1
    else:
        target_dict[word] = 1

sentence = '''Nittin & his mom went to a park last friday. 
            His Mom observed that the weather was too cool. 
            Nittin also met his sis. 
            If we reverse the number 1331 then we also get 1331.'''

word = ''
pallindrome_counts = {}

for index, char in enumerate(sentence):
    if char in ' .,':
        if is_pallindrome(word.lower()):
            word_counter(pallindrome_counts, word.lower())
        word = ''
    else:
        word += char

print(pallindrome_counts)


# 23. create 2 dictionaries as follows:
# dict1 = {'name': 'Msys', 'Place': 'Pune'}
# dict2 = {'EmpID': 0001, 'Salary': 50000}
# Perform following operations:
# a. create single dictionary by merging dict1 & dict2
# b. update the salary to 10%
# c. update age to 35
# d. extract & print all the values & keys separetly in tuple.
# e. delete the element with key 'Age' & print the dictionary elements.

def dict_merger(target_dict, original_dict, filter_key=None):
    for key in original_dict:
        if key != filter_key:
            target_dict[key] = original_dict[key]

dict1 = {'name': 'Msys', 'Place': 'Pune'}
dict2 = {'EmpID': '0001', 'Salary': 50000}

emp_dict = {}
dict_merger(emp_dict, dict1)
dict_merger(emp_dict, dict2)

emp_dict['Salary'] += emp_dict['Salary'] * 10 / 100
emp_dict['Age'] = 35

# print(emp_dict)

keys = ()
values = ()

for key in emp_dict:
    keys += (key, )
    values += (emp_dict[key], )

print(keys)
print(values)

# del emp_dict['Age']
new_emp_dict = {}
dict_merger(new_emp_dict, emp_dict, 'Age')
print(new_emp_dict)


# 24. You have given a string str1 = "abcbaefabcabchijkl"
# your task is to find the combination of given word without repetition, present in the string , given 
# word 'abc'
# o/p = 7
# explaination :
# abc, cba,
# cba,
# bca, acb
# cab, bac

def fact(num):
    if not num:
        return 1

    return fact(num-1)

str1 = 'abcbaefabcabchijkl'
word = 'abc'
word_len = len(word)

res = fact(n) 
print(res)

# abc
# acb
# bac
# bca
# cab
# cba

# 25. Given an Integer n, count the total number of times 1 is appearing in all non-negative integers 
# less than or equal to n.
# Ex – n = 13, output should be 6
# method – 1 is coming 6 times starting from number 0 till 13 in ‘1’, ‘10’, ‘11’, ‘12’, ‘13’. Also note 1
# is coming 2 times in 11. That is why 6 is the output

def one_counter(num):
    no_of_ones = 0

    while num:
        if num % 10 == 1:
            no_of_ones += 1
        num //= 10

    return no_of_ones

n = 13
count_ones = 0

for num in range(n+1):
    count_ones += one_counter(num)

print(count_ones)