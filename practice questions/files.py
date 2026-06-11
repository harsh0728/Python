#1
# f=open("practice.txt","w")
# data="Hi everyone\n we are learning File Input/Output\n using Java, \nI like Programming in Java."
# f.write(data)
# f.close()

# or another way to write in a file
with open("practice.txt","w") as f:
    data="Hi everyone\nwe are learning File Input/Output\nusing Java, \nI like Programming in Java."
    f.write(data)

#2
with open("practice.txt","r") as f:
    data=f.read()

new_data=data.replace("Java","Python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)


#3
new_data=new_data.count("learning")
print("The word 'learning' appears",new_data,"times in the file.")

# or another way to count the word "learning" in the file
def find_word():
    with open("practice.txt","r") as f:
        data=f.read()
        if(data.find("learning")!=-1):
            print("Found 'learning' in the file.")
        else:        
            print("'learning' not found in the file.")

find_word()

#4
def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if (word in data):
                print(line_no,":",data)
                return
            line_no += 1
    return -1

check_for_line()

#5

def check_even():
    count=0
    with open("nums.txt","w") as f:
        f.write("1,2,3,4,5,6,7,8,9,10")
    with open("nums.txt","r") as f:
        data=f.read()

        nums=data.split(",")
        for val in nums:
            if (int(val)%2==0):
                print(val,"is an even number.")
                count+=1
    print("Total even numbers in the file:",count)

check_even()