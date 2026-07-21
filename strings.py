#string- a sequence of characters
first_name = "reece"
last_name = 'james'
print(f'My first name is, {first_name}')
# +  concatenation
fullname =first_name + " " + last_name
print(fullname)
#f-string f""
age = 19
print(f"my name is {fullname} and I am {age} years old")
#string methods upper(),lower(),find(),replace()
message = "hello world"
print(message.upper())
# capitalize 
print(message.capitalize())
#lower ()
print(message.lower())
#find ()
print(message.find("e")) #finds the index
print(message.replace('world','goodmorning'))
#slicing/substring [start:stop:step]
course = "python"
print(course)
print(course[0:3]) #from zero to two
print(course[1:]) #1-end
print(course[:4]) #0-3
print(course[::2])
#text="fullstack"
#full
#stack
#fullsta
course = "fullstack"
print(course[0:4])
print(course[4:])
print(course[:7])
#escape characters /n-newline,/t-tab
print("hello this \n is python")
# \t -tab - adds a tab space
print("name \t: age")
# \' - adds a single quote
print('it\'s a nice day')
# \" - adds a double quote
print("she said \"hello\"")
# she said "I love python programming"
print("she said \"I love python programming\"")
#"python is easy"- john kelly
print("\"Python is easy\"-John Kelly")