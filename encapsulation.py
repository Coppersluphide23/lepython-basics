#encapsulation is process of hiding data (properties) and methods
#inside a class
#controlling how its acessed or modified
#you make an attribute private by adding two underscores(__)
class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age #age is a private property/attribute

    #use a getter method to access private property
    def get_age(self):
        return self.__age
    #setter method used to change a private attribute
    def set_age(self,age):
        #validation
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive!!")
#create an object
person1 = Person("Mike",20)
#accessing the attributes
print(person1.name)
print(person1.get_age())
#update age
person1.set_age(19)
print(person1.get_age())