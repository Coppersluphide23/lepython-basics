#function with return keyword- return a value when called
#function that adds 2 numbers
def addTwoNumbers(a,b):
    sum=a+b
    return sum
#calling the function
result=addTwoNumbers(36,45)
print('The sum is',result)
#way 2
print(addTwoNumbers(36,45))
#function that multiplies 3 numbers
def multiply(x,y,z):
    return x*y*z
#calling the function
print(multiply(5,70,40))
#function that checks if a number is even or odd
def evenOrOdd(num):
    if num%2==0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')   
#gets the number from the user
mynum=int(input('Enter a number to check if even or odd'))
#calling the function
evenOrOdd(mynum)