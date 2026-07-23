#list used to store multiple items in a single variable
#listname[itmem1,item2,item3,]
students= ["Jane","Kamau","John","Mary"]
print(students)
print(type(students))
myscore = [90,34,56,78,91]
print (myscore)
#accessing list items
print(students[0])
print(myscore[3])
print(students[3])
#change list item
students[1]="William"
print(students)
#list methods append(),remove(),pop()
#append()-add an item to the end of the list
students.append("Cate")
print(students)
#remove() - removes a specific item
students.remove("John")
print(students)
#sort - sorts alphabetically
myscore.sort()
print(myscore)
#looping through a list
for x in students:
    print (x)
for y in myscore:
    print(y)    