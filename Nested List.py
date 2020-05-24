#Program to find student with second lowest marks
#python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

no_of_student = int(input("Enter number of students data you want to enter: "))
count = range(no_of_student)
n = 1
student_list = []
names_list = []
marks_list = []
while n>0 and n <= no_of_student:
    name = input(f"Enter student {n} name: ")
    score = float(input(f"Enter student {n} marks: "))
    student_list.append([name, score])
    names_list.append(name)
    marks_list.append(score)
    n += 1

sorted_marks = sorted(marks_list,reverse=True)
print(sorted_marks)
while sorted_marks[-1] == sorted_marks[-2]:
    lowest_mark = sorted_marks[-2]
    sorted_marks.remove(sorted_marks[-1])
    print(f"Lowest marks is {lowest_mark}")
else:
    second_lowest = sorted_marks[-2]
    print(f"Second Lowest marks is: {sorted_marks[-2]}")

for list in student_list:
    if second_lowest == list[1]:
        print(f"Second Lowest marks are of: {list[0]}")
