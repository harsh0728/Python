dict={
    "name":"John",
    "age":30,
    "city":"New York"  ,
    "hobbies":["reading","traveling","swimming"],
    "is_student":False,
    "subjects":{
        "math":85,
        "science":90,
        "english":88
    } 
}
print("The dictionary is: ",dict," ",type(dict))
print("Name: ",dict["name"])
dict["age"]=31
print("Updated Age: ",dict["age"])

# Dictionary Methods
print(dict.keys())
print(dict.values())
print(dict.items())
dict["country"]="USA"
print("After Adding Country: ",dict)
dict.pop("hobbies")
print("After Removing Hobbies: ",dict)

get_subjects=dict.get("subjects")
print("Subjects: ",get_subjects)

updated_subjects={"math":90,"science":95,"english":92}
dict.update({"subjects":updated_subjects})
print("After Updating Subjects: ",dict)