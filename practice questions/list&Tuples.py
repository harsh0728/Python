# movies=[]
# first_movie=input("Enter the name of the first movie: ")
# second_movie=input("Enter the name of the second movie: ")
# third_movie=input("Enter the name of the third movie: ")

# movies.append(first_movie)
# movies.append(second_movie)
# movies.append(third_movie)
# print("The movies you entered are: ",movies," ",type(movies))

list=[1,2,3,4,5,4,3,2,1]
print("The list is: ",list," ",type(list))

list1=list.copy()
print("The copied list is: ",list1," ",type(list1))

list1.reverse()

if (list1==list):
    print("The original list and the copied list are the same and palindrome.")
else:
    print("The original list and the copied list are different and not palindrome.")


grades=("C", "D", "A", "A", "B", "B","A")
print ("No. of students who got A grade: ",type(grades)," ",grades.count("A"))

grades_list=["C", "D", "A", "A", "B", "B","A"]
print("The list converted from tuple is: ",grades_list," ",type(grades_list))
grades_list.sort()
print("Sorted list: ",grades_list)