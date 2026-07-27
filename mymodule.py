# module is a python file that contains reusable code,eg functions,variables etc
#types of modules - in built modules-eg math modules,random modules,datetime modules,os modules,system modules
#user defined modules-you create your own
import math
import random
import datetime
import os
import sys
print(math.sqrt(25))
print(math.pi)
print(math.floor(4.4766))
print(math.ceil(4.4766))
#generating random numbers
print(random.random())
#generate random int btwn 5,10
print(random.randint(5,10))
#get current date and time
print(datetime.datetime.now())
#print current date
print(datetime.date.today())
#prints the current working directory
print(os.getcwd())
#checks platform
print(sys.platform)
print(sys.version)

#user defined module