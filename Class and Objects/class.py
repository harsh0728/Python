# Class and Objects
class Student:
    def __init__(self,name,marks):                    # Constructor
        self.name=name
        self.marks=marks
        print ("Constructor defined")

    def welcome(self):
        print("Welcome",self.name)

    def get_marks(self):
        return self.marks

s1=Student("Harsh",92.4) #objects
s1.welcome()
print(s1.get_marks())



