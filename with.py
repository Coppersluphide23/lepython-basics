#with ..as
with open("opera.txt","w") as x:
    x.write("hello, goodmorning")
    x.write('\n Mr.West')
#read
with open("opera.txt","r") as file:
    print(file.read())