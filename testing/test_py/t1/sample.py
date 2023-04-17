# def add(a, b):
#     return a + b

    
class Car:
    wheels = 4

    def __init__(self, color):
        # print("self", id(self))
        self.color = color

tesla = Car("black")
# print("tesla", id(tesla))
# tata = Car("red")

nano = Car("green")

print(Car.wheels)
print(nano.wheels, nano.color)
print(tesla.wheels, tesla.color)

Car.wheels = 5

print(Car.wheels)
print(nano.wheels, nano.color)
print(tesla.wheels, tesla.color)


tesla.wheels = 10
print(Car.wheels)
print(nano.wheels, nano.color)
print(tesla.wheels, tesla.color)