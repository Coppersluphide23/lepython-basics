#function is a block of code that does a specific task
#the code only runs when its called
def functionname():
    # body of the function
    print("Function is called")

# calling the function
functionname()
def greetings():
    print('hello!,good morninhg')
#calling the function
greetings()
greetings()
greetings()    
#function with parameter
def hello(first_name):
    print('hello, how are you',first_name)
#calling the function
hello('Jane')
hello('Ramirez')
#function with multiple parameters
def opera(name,age,course='mit'):
    print(f'Student name is {name}, he is {age} years old and studying {course}')
#calling the function
opera('Mike',18,'MIT')
opera('Lucas',19,'Cybersecurity')
opera('Jake',21)
#functions that calculate area of a rectangle(LxW)
def area0fRectangle(l,w):
    area = l * w
    print(f'The area of rectangle with length {l} and width {w} is {area}')

#calling the function
area0fRectangle(10,90)
area0fRectangle(45,34)

#function that calculates area of a circle  A=(3.14*R*R)
def area0fCircle(r):
    area = 3.14 * r * r
    print(f'The area of a circle with radius {r} is {area}')

#calling the function
area0fCircle(10)
area0fCircle(2.5)
