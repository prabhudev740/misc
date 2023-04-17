# 3. Given a tuple (“Msys”, “Technologies”, “2007”), add “Python” at the end of this tuple and the 
# output should also be in the form of tuple. Make a note that tuples are immutable in nature so you 
# need to find some idea to make modification and print the updated tuple.

data = ("Msys", "Technologies", "2007")

# method 1
res1 = tuple(list(data) + ["Python"])

# method 2
res2 = (data) + ("Python", )

print(res1)
print(res2)



# 4. In the dictionary {‘India’:’New Delhi’, ‘USA’:’Washington D.C.’, ‘Nepal’:’Kathmandu’} list out 
# all the keys in a list named as ‘list_keys’ and list out all the values in a list named as ‘list_values’. 
# Also find out the value of key ‘Australia’ in the list and as it is not existing in the list print ‘NA’ as 
# its value.

capital_dict = {'India':'New Delhi', 'USA':'Washington D.C.', 'Nepal':'Kathmandu'}

list_keys = [key for key in capital_dict]
list_values = [capital_dict[key] for key in capital_dict]

print(list_keys)
print(list_values)


# 5. Given a dictionary {‘Msys Technologies’:’Sanjay Sehgal’, ‘Infosys’:’Salil Parekh’, 
# ‘TCS’:’Rajesh Gopinathan’, ‘Wipro’:’Thierry Delaporte’} make a list of all the values associated 
# with keys in alphabetically sorted order.



# 6. Write a program to extract the words starting with lowercase letter present in the list. [‘Nissan’, 
# ‘maruti’, ‘hyundai’, ‘Volkswagen’, ‘audi’]

car_list = ['Nissan', 'maruti', 'hyundai', 'Volkswagen', 'audi']

for car in car_list:
    if car and car[0].islower():
        print(car)

print()
for car in car_list:
    if car and 'a' <= car[0] <= 'z':
        print(car)


# 7. Write a program using dictionary comprehension which will contain the key value pair of i:i**2. 
# Value of ‘i’ will start from 1 and will go upto 10.

start_i = 1
end_i = 10

square_dict = {i : i ** 2 for i in range(start_i, end_i + 1)}

print(square_dict)


# 8. Take the input marks from user using input() function and find out the grade of the students. Note
# the grading will be in this manner – (100 – 91) – A1, (90-81) – A2, (80-71) – B1, (70-61) – B2, (60-
# 51) – C1 (50-40) – C2 and less than 40 students will ‘Fail’. Also make sure user should input the 
# marks in the range 0<=marks<=100, if user will input some other marks in should print invalid 
# marks.

def get_grade(mark):
    if 91 <= mark  <= 100:
        print("A1")
    elif 81 <= mark  <= 90:
        print("A2")
    elif 71 <= mark  <= 80:
        print("B1")
    elif 61 <= mark  <= 70:
        print("B2")
    elif 51 <= mark  <= 60:
        print("C1")
    elif 41 <= mark  <= 50:
        print("C2")
    else:
        print('Fail')


print("Please enter a value between 0 to 100")
while True:
    mark = int(input())

    if 0 <= mark <= 100:
        get_grade(mark)
        break
    else:
        print("Incorrect Mark!!!  Please enter a value between 0 to 100")