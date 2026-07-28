#class is a blueprint for creating objects
class Car:
    #constructor
    #automatically called when an object is created
    def __init__(self,brand,model,color,year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
    def __str__(self):
        return f'The car is a {self.brand} {self.model} {self.color} {self.year}'
    #method to display car details
    def display_info(self):
        return f'The car is a {self.color} {self.brand} {self.model} made in the year {self.year}'
    #method to get car age
    def car_age(self):
        return f'The car is {2026-self.year} years old'
#creating an object
# onject is an instance of a class
car1 = Car('BMW','X5','white',2020)
car2=Car('Mercedes','W124',"grey",1995)
#accesssing attributes
print(car1.brand)
print(car1.model)
print(car1.color)
print(car1.year)
print(car1)
print(car1.display_info())
print(car2.display_info())
print(car2.car_age())