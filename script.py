import newmodule
print(newmodule.first_name)
print(newmodule.addTwoNumbers(56,90))
print(newmodule.displayDetails("matthew","mit"))
from newmodule import addTwoNumbers,displayDetails
print(addTwoNumbers(67,89))
print(displayDetails("lewis","Cybersecurity"))
import newmodule as nm 
print(nm.first_name)
print(nm.addTwoNumbers(23,56))
print(nm.displayDetails('Mark','Data Science'))