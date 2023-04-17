
# 17. Write a program to find the count of alphabet alone in the given alphanumeric string for 
# Ex1: input=’abb24ccc8ddbbca1’ output=’a1b224c3d2b2c1a11’ 
# Ex2: input = ‘abc23’ output=’a1b1c123

def char_counter(s):
    result = temp = ""
    char_count = 0

    for index, char in enumerate(s):
        if char.isalpha():
            if not char_count:
                temp = char
                result += char
                char_count = 1
            elif char_count and temp == char:
                char_count +=1
            else:
                result += str(char_count)
                temp = char
                result += char
                char_count = 1
                
            if index == len(s) - 1:
                result += str(char_count)
        else:
            if char_count:
                result += str(char_count)
                char_count = 0

            result += char 

    return result


print(char_counter("abc23")) #a1b1c123
print(char_counter("aa9aa")) #a29a1
print(char_counter("aabb24ccc8ddbbca1")) #a2b224c38d2b2c1a11
print(char_counter("abb24ccc8ddbbca1")) # ’a1b224c3d2b2c1a11’
print(char_counter("1"))
print(char_counter(""))
print(char_counter("a"))
print(char_counter("aa"))

# 18. Write a python program where for every two hours it prints the pattern without using 
# sleep function 
# *********
# *******
# *****
# ***
# * 

from datetime import datetime

def print_stars(cols):
    for cul in range(1, cols*2):
            print("*", end="")
    print()


rows = row_no = 5
preveous = datetime.now()

while row_no:
    current = datetime.now()
    if not rows - row_no or current.min - preveous.min == 120:
        print_stars(row_no)

        preveous = current
        row_no -= 1

# 19. Write a program using decorators to print the traffic signal messages 
# Expected output - 
# RED : STOP 
# YELLOW : SLOW DOWN 
# GREEN : GO 
# The decorator should be working in this order 

def traffic(func):
    def inner(light):
        x = func(light).upper()
        if x == "RED":
            return f"{x} : STOP"
        elif x == "YELLOW":
            return f"{x} : SLOW DOWN"
        else:
            return f"{x} : GO"

    return inner

@traffic
def signal(light):
    return light

print(signal("Red"))

# 20. Write a python program for sort the given below list based last character of each word 
# names_list = ['Prabhu', Rahul', 'Arunesh, 'Sonali', 'Rakshit'] 

def selection(A):
    n = len(A)

    for i in range(n):
        pos = i
        last_char_of_pos = len(A[pos]) - 1

        for j in range(i+1, n):
            last_char_of_j = len(A[j]) - 1

            if A[j][last_char_of_j] < A[pos][last_char_of_pos]:
                pos = j
                last_char_of_pos = len(A[pos]) - 1
            

        A[i], A[pos] = A[pos], A[i]

names_list = ['Prabhu', 'Rahul', 'Arunesh', 'Sonali', 'Rakshit'] 
selection(names_list)
print(names_list)

# we can open a large file using open() function in read mode.
# But if we read the data at once it will crash the code.
# To prevent that we can read small portion or size of data at once.

# Here is an example for same with a text file.

# 21. How do you open a file of large size, say around 10GB? So that program should not 
# crash 
with open("testfile.py", "r") as fp:
    while True:
        part = fp.read(1024 * 1024)

        if not part:
            break

# 22. Write a function where month and year are taken as arguments which returns the output 
# with all the dates of saturdays occuring the month 

def get_saturdays_in_month(month, year):
    if month in [4, 6, 9, 11]:
        num_days = 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            num_days = 29
        else:
            num_days = 28
    else:
        num_days = 31
    
    saturdays = []
    for day in range(1, num_days+1):
        weekday = (year + (year // 4) - (year // 100) + (year // 400) + ((13 * month + 8) // 5) + day) % 7
        
        if weekday == 6:  
            saturdays.append(day)
    
    return saturdays

print(get_saturdays_in_month(3, 2023))

# 23.
def max_sum_without_duplicates(s):
            max_sum = 0
            seen = set()
            curr_sum = 0
            for c in s:
                if c not in seen:
                    seen.add(c)
                    curr_sum += int(c)
                else:
                    max_sum = max(max_sum, curr_sum)
                    seen = {c}
                    curr_sum = int(c)
            max_sum = max(max_sum, curr_sum)
            return max_sum

print(max_sum_without_duplicates('1211'))