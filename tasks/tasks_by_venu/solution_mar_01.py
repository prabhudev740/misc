# 4. What is the importance of PEP rules 
# 5. Can we order a dictionary? How? 
# 7. Difference between append and extend operations of list 
# 8. Create a dictionary where the key is an even number from the given list and the value 
# will be the occurrence of that element in the list. input= [1,2,3,2,4,2,4,7,8,4,5,8,6,9,2] 
# 9. Write a function swap_element that contains two args which will be the position of 
# elements present in the list. The function must swap the elements present in those 
# positions. 
# Input: [1,2,3,4,5,6,7,8] function: swap_element(arg1, arg2) 
# 10. Write the output of the program: 
# match = ‘version’, input=’Upgraded_image_version_8.0.4.3’ 
# if match in input: 
# print(‘YES’) 
# else: 
# print(‘NO’)


# Solution 4
# ---------------
# PEP stands for Python Enhancement Proposal

# These are the set of guidlines and recommendations a developer can follow to write clean codes.
# These rules have some standards, if we follow them other developers can read our codes easily

# This is important to apply PEP rules, because it increseases readability and consistency in our code and
# alse makes our codes compatible with other libraries and frameworks

# Solution 5
# -----------
# Yes, There is OrderedDict, this is a dict which can keet the order of keys as they inserted in dict

# Previously, python dict was storing the data random way. But now after Python 3.7 Python 
# also stores data in ordered manner.

# We can sort a dict using sorted() function.

name_counts = {"Vijay": 2, "Ajay": 3, "Sanjay":1}
print(name_counts)

ordered_name_counts = dict(sorted(name_counts.items()))
print(ordered_name_counts)

# Solution  7
# ------------
# append and extend both are list methods

# while append will add one element at the end of list object, entend is used to add a collection
# element to the end of list objrct.

# append will take a object and add at the end
# extend will take a collection add all the element to at the end of list

# both will not return anything, i.e. they will make the change inplace without creating new list.

# Examples are given below.

# append
num_list = [1, 2, 3, 4]

new_num = int(input())
print(f"num list before append: {num_list}")
num_list.append(new_num)
print(f"num list after append: {num_list}")

# extend
num_list = [1, 2, 3, 4]

new_list = [100, 200, 300]
print(f"originalnum list: {num_list}")
print(f"after extendinag a list to num list: {num_list}")
num_list.extend(new_list)

# Solution 8 - get dict with count of even no.s
input= [1,2,3,2,4,2,4,7,8,4,5,8,6,9,2] 

even_counts = {}

for num in input :
    if not num % 2:
        if num not in even_counts:
            even_counts[num] = 1
        else:
            even_counts[num] += 1

print(even_counts)

# Solution 9 -- Swap value at index
Input = [1,2,3,4,5,6,7,8] 
def swap_element(arg1, arg2) :
    global Input
    Input[arg1], Input[arg2] = Input[arg2], Input[arg1]

print("Original input is", Input)
swap_element(4, 5)
print("Input after swapping", Input)


def swap_positions(arr, pos1, pos2):
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp

arr = [1, 2, 3, 4, True]
print("list is ", arr)

swap_positions(arr, 0, 4)
print("list after swapping is ", arr)

# Solution 10
# -------------
# 10. Write the output of the program: 
# match = ‘version’, input=’Upgraded_image_version_8.0.4.3’ 
# if match in input: 
# print(‘YES’) 
# else: 
# print(‘NO’)

# Output --> YES