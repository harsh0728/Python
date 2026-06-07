dict={
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts and figures"],
}
print("The dictionary is: ",dict," ",type(dict))

my_set={"python","java","c++","python","javascript","java","c++","python","java","c"}
print("The set is: ",my_set," ","Classrooms required: ",len(my_set)," ",type(my_set))

subjects={}
x=input("Enter the name of the phy subject: ")
subjects.update({"phy": x})
x=input("Enter the name of the second subject: ")  
subjects.update({"chem": x})
x=input("Enter the name of the third subject: ")
subjects.update({"bio": x})
print("The subjects dictionary is: ",subjects," ",type(subjects))


values={'9',9.0,("int",8),("float",8.0)}
print("The set of values is: ",values," ",type(values))