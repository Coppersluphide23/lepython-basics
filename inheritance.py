#inheritance is a concept in OOP that allows a child class or sub class to inherit
#attributes and methods from another class (called the parent ? super class)
#This promotes code reusability and reduces redundancy
#parent class
class Animal:
    #constructor
    def __init__(self,name,age):
        self.name = name
        self.age = age
#method
    def __str__(self):
        return f'The animal name is {self.name}, Age{self.age}'
#method
    def eat(self):
        return f'{self.name} is eating'
#child class inherits from parent class(Animal to Dog)
class Dog(Animal):

    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed = breed

    def speak(self):
        return f'{self.name} says woof woof!!'

    def display_info(self):
        return f'Name: {self.name} Age:{self.age},Breed: {self.breed}'
    
#another child class of Animal
class Cat(Animal):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color
    def speak(self):
        return f'{self.name} says meow meow'
    def display_info(self):
        return f'Name: {self.name}, Age: {self.age} and Color: {self.color}'
     
            
    
#create a dog object
dog1 = Dog('Simba',4,'Shitzu')
print(dog1)
print(dog1.eat())

#call speak
print(dog1.speak())
print(dog1.display_info())

#create a cat object
cat1=Cat('Kitty',2,'white')
print(cat1.speak())
print(cat1.display_info())
print(cat1.eat())