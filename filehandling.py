#creating reading,writing,updating and delting files using python
#open function open()
# open(filename,mode)
#modes-read(r),write(w),append(a)
#write -w- to write to file
x=open("demo.txt","w")
x.write("hello! this is python")
x.close()
#read-to read from a file open it in read mode
#to read the contents,use read()method
y=open("demo.txt","r")
print(y.read())
y.close()
#append = adding content to an existing file without overwriting what is already there
#open in append mode(a)
open("demo.txt","a")
z=open('demo.txt','a')
z.write('\n this is some appended text')
z.close()

#read the contents of the file
file=open("demo.txt","r")
print(file.read())
file.close()