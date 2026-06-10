f=open("demo.txt","r")
data=f.read()
print(data)

f=open("demo.txt","a")
f.write("\nThis is a new line.")    

f.close()

with open("file.txt","w") as f:
    f.write("This is a new file created using with statement.")

import os

os.remove("file.txt")