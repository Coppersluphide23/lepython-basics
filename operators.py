#Operators used to perform operations on variables and values
#arithmetic operators
# +,-,*,/,%
#addition +
x = 10
y = 35
sum = x+y
diff = y-x
print("The sum is",sum)
#substraction -
print(f"The difference is,{diff}")
#multiplication *
print(f"The product of {x} and {y} is {x*y}")
#Division /
print(f"The division of {y} and {x} is {y/x}")
#Modulus % - the remainder of division
print(f"The modulus of {y} and {x} is {y%x}")
# Exponent ** (power)
print(x**3)
#comparison operators.>,<,>=,<=,==,!=
#greater than >
print(f"Is {x} greater than {y}? {x>y}")
#less than<
print(f"Is {x} lesser than {y}? {x<y}")
#equality ==
print(x==y)
#greater than or equal to >=
print(x>=y)
#less than or equal to <=
print(x<=y)
#not equal to !=
print(x!=y)
#logical operaors - AND,OR and NOT
#AND - returns true if both statements are true
z = 5
print(z>3 and z<10)
print(z<3 and z<10)
#OR - returns true if one of the statements is true
print(z<3 or z<10) 
#not - returns the reverse
print(not(z<3))
#Assignment operators -=,+=,*=,/=\
a = 20
print(a)
# +=
a+=5 # a=a+5
print(a)
# -=
a-=2 #a=a-2
print(a)