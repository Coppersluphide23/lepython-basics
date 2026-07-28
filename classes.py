class Student:
    #attributes-name,age course,score
    #constructor - method that runs automatically when making an object(__init__)
    def __init__(self,first_name,age,course):
        self.first_name = first_name
        self.age = age
        self.course = course
    #returns a readable string object    
    def __str__(self):
        return f"Student name is {self.first_name}, he is {self.age} years old and he's studying {self.course}"
    #method that returns student email
    def get_email(self):
        return f'{self.first_name}@emobilis.co.ke'
    #A method that displays age
    def display_age(self):
        return f'{self.first_name} is {self.age} years old'
#creating an object
#object is an instance of a class
#objectname=classname(values)
student1=Student("Andrew",18,"MIT")
print(student1.first_name)
print(student1.course)
print(student1.age)
print (student1)
student2=Student("Mike",21,"Cybersecurity")
print(student2.first_name)
print(student2.course)
print(student2.age)
print(student2)
#create another object
student3 =Student("Leon",19,'Data Science')
#Accessing our parameter values
print(student3.first_name)
print(student3.course)
print(student3.age)
#calling the get email()
print(student1.get_email())
print(student2.get_email())
print(student3.get_email())
#call the display_age()
print(student1.display_age())
print(student2.display_age())
print(student3.display_age())
