class Student:
    #attributes-name,age course,score
    #constructor - method that runs automatically when making an object(__init__)
    def __init__(self,first_name,age,course):
        self.first_name = first_name
        self.age = age
        self.course = course
    #returns a readable string object    
    def __str__(self):
        return f"Student name is {self.first_name}, age: {self.age} and course: {self.course}"
#creating an object
#object is an instance of a class
#objectname=classname(values)
student1=Student("Andrew",18,"MIT")
print(student1.first_name)
print(student1.course)
print(student1.age)
print (student1)
student2=Student("mike",21,"Cybersecurity")
print(student2.first_name)
print(student2.course)
print(student2.age)
print(student2)
