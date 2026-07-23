#dicttionary are used to store data values in key:value pair
student={
    'name': "otieno",
    "age": 17,
    "course": "MIT"
}
print(student)
print(type(student))
#add key : value pair
student["city"] = "Nairobi"
print(student)
#accessing items[]
print(student["city"])
print(student["name"])
#change a value in dictionary
student["name"] = "Mike"
print(student)
#keys() - returns a list of all the keys in the dictionary
print(student.keys())
#values() - returns a list of all the values in the dictionary
print(student.values())
#items() - returns a list containing  a tuple for each key value pairs
print(student.items())
#loop
for x,y in student.items():
    print(x,":",y)