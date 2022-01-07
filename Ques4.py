# Question 4 : Make a list to enter marks of 5 students into a list and display them in a sorted manner.

student1_marks = int(input("Enter the marks of the Student 1: "))
student2_marks = int(input("Enter the marks of the Student 2: "))
student3_marks = int(input("Enter the marks of the Student 3: "))
student4_marks = int(input("Enter the marks of the Student 4: "))
student5_marks = int(input("Enter the marks of the Student 5: "))

student_markslist = [student1_marks, student2_marks, student3_marks, student4_marks, student5_marks]
print("\n List of the Student Marks:\n ", student_markslist)

# Sorted List
print("\n Sorted Student List (increasing order): ")
student_markslist.sort()
print(student_markslist)