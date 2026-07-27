#try and except is used for exception handling
"""
try:
    block of code that can cause an error
except:
    code that runs if an error occurs
"""
try:
    num=int(input('enter a number'))
    print(10/num)
except ZeroDivisionError:
    print('you cannot divide by zero')
#name error
try:
    x = 5
    print(x)
except NameError:
    print('variable is not defined')
#using else...try..except..else.
#else block runs if no exception occurs
try:
    age=int(input("enter your age: "))
except ValueError:
    print('please enter a valid number')
else:
    print(f'you are {age} years old')