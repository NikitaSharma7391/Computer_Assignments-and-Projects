# QUESTION 1: To count the number of occurrences of each word or character in the string entered by the user.

string1 = input("Enter a string:\n")

#To split all the elements present in the string and stored in a list.
list = string1.split()
dict = {}

#To count the number of occurrences of each character when only the single word is entered by the user.
if list.__len__()==1:
    for i in list[0]:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i]=1
    print("The number of occurrences of each character when only the single word is entered:\n",dict)

#To count the number of occurrences of each word present in the string.
else:
    for i in list:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i]=1
    print("The number of occurrences of each word present in the string:\n",dict)
print(" \n ")


# QUESTION 2: To print the next date of input date (use if-elif).

def Next_Date():
    List1 = [1, 3, 5, 7, 8, 10]
    List2 = [4, 6, 9, 11]
    List3 = [2]
    List4 = [12]

    while (True):
        day = int(input("Enter the day:\n"))
        if (1 <= day <= 31):
            break
        else:
            print("Invalid Day !!\n")

    while (True):
        month = int(input("Enter the month:\n"))
        if (1 <= month <= 12):
            break
        else:
            print("Invalid Month !!\n")

    while (True):
        year = int(input("Enter the year (1800 to 2025):\n"))
        if (1800 <= year <= 2025):
            break
        else:
            print("Invalid Year !!\n")

    if month in List1 :
        if (day == 31):
            day = 1
            month = month + 1
            print("Next Date is:  ", day, "/", month, "/", year)
        elif (day < 31):
            day = day + 1
            print("Next Date is:  ", day, "/", month, "/", year)
        else:
            print("Invalid Date !!\n")
            Next_Date()

    elif month in List2 :
        if (day == 30):
            day = 1
            month = month + 1
            print("Next Date is:  ", day, "/", month, "/", year)
        elif (day < 30):
            day = day + 1
            print("Next Date is:  ", day, "/", month, "/", year)
        else:
            print("Invalid Date !!\n")
            Next_Date()

    elif month in List3:
        if (year % 4 == 0):
            if (day == 29):
                day = 1
                month = month + 1
                print("Next Date is:  ", day, "/", month, "/", year)
            elif (day < 29):
                day = day + 1
                print("Next Date is:  ", day, "/", month, "/", year)
            else:
                print("Please enter the valid date !!\n")
                Next_Date()
        else:
            if (day == 28):
                day = 1
                month = month + 1
                print("Next Date is:  ", day, "/", month, "/", year)
            elif (day < 28):
                day = day + 1
                print("Next Date is:  ", day, "/", month, "/", year)
            else:
                print("Please enter the valid date !!\n")
                Next_Date()

    elif month in List4:
        if (day == 31):
            day = 1
            month = 1
            year = year + 1
            print("Next Date is:  ", day, "/", month, "/", year)
        elif (day < 31):
            day = day + 1
            print("Next Date is:  ", day, "/", month, "/", year)
        else:
            print("Please enter the valid date !!\n")
            Next_Date()
    else:
        print("Please enter the valid date !!\n")
        Next_Date()

Next_Date()
print("\n")


""" QUESTION 3: To create a list of tuples with the first element as the number
     and Second element as the square of the number. """

inp_list = input("Enter elements in a list separated by spaces:\n")
List = inp_list.split()
print("The Required List is:\n",inp_list)

for i in range(len(List)):
    List[i] = int(List[i]) # Conversion of each element into int datatype.
updated_list =[(List[i], List[i] ** 2) for i in range (len(List))]
print("Updated List after squaring is:\n",updated_list)
print("\n")


""" QUESTION 4: To prompt the user for a grade between 4 and 10. If the grade
     is out of range print error message. """

grade = int(input("Enter your Grade between 4 tO 10: \n"))
if( grade == 4 ):
    print("Your Grade is 'D' and Poor Performance.")
elif( grade == 5 ):
    print("Your Grade is 'C' and Below Average Performance.")
elif( grade == 6 ):
    print("Your Grade is 'C+' and Average Performance.")
elif( grade == 7 ):
    print("Your Grade is 'B' and Good Performance.")
elif( grade == 8):
    print("Your Grade is 'B+' and Very Good Performance.")
elif( grade == 9 ):
    print("Your Grade is 'A' and Excellent Performance.")
elif( grade == 10 ):
    print("Your Grade is 'A+' and Outstanding Performance.")
else:
    print("Error !!")
print("\n")


#  QUESTION 5:

Word = "ABCDEFGHIJK"

count = 1
print("The Pattern is:\n")

while(count<7):
    print(" " * (count - 1), Word[0:11-((count-1) * 2)])
    count += 1
print("\n")


#  QUESTION 6:

student_info = {}
n = "y"

# (A) : Print students details stored in the dictionary.
print("(A)")
while(n == "y"):
    sid = int(input("Enter the SID:\n"))
    name = input("Enter the Student's name:\n")
    student_info[sid] = name
    n = input("Want to enter any other Student Details ??\nEnter a letter y (if Yes) or n (if No):\n")
print("The Required Student Details stored in the Dictionary: \n",student_info)

# (B) : Sort dictionary using student names.
print("\n (B)")
sort_by_name = {k:v for k,v in sorted(student_info.items(), key=lambda v:v[1])}
print("Sorting Dictionary using Student Names: \n",sort_by_name)

# (C) : Sort dictionary using SID.
print("\n (C)")
sort_by_sid = {k:v for k,v in sorted(student_info.items())}
print("Sorting Dictionary using SID: \n",sort_by_sid)

# (D) : Search a student details with SID and print name of that student.
print("\n (D)")
entered_SID = int(input("Search a student details with SID that you entered before: \n"))
print("The name of that Student is: ")
print(student_info[entered_SID])
print("\n")


# QUESTION 7: To print Fibonacci sequence also print average of the resultant Fibonacci series.

def fibo_recursive(n):
   if n <= 1:
       return n
   else:
       return (fibo_recursive(n-1) + fibo_recursive(n-2))

nterms = int(input("Till how many terms you want to print: \n"))
# Check if the number of terms is valid
if nterms <= 0:
   print("Please Enter a Positive Integer !!")
else:
   print("Fibonacci sequence is:")
   sum = 0
   for i in range(nterms):
       print(fibo_recursive(i))
       sum = sum + fibo_recursive(i)

average = float(sum / nterms)
print("Average of the resultant Fibonacci Sequence: \n",average)
print("\n")


#  QUESTION 8:

Set1 = {1,2,3,4,5}
Set2 = {2,4,6,8}
Set3 = {1,5,9,13,17}

#(a) : Create a new set of all elements that are in Set1 and Set2 but not both.
print("(a)")
new_set = (Set1 | Set2) - (Set1 & Set2)
print(new_set)
print("\n")

#(b) : Create a new set of all elements that are in only one of the three sets: Set1, Set2 and Set3.

print("(b)")
new_set = (Set1 | Set2 | Set3) - ((Set1 & Set2) | (Set1 & Set3) | (Set3 & Set2))
print(new_set)
print("\n")

#(c) : Create a new set of elements that are exactly two of the sets Set1, Set2 and Set3.
print("(c)")
new_set = ((Set1 & Set2) | (Set1 & Set3) | (Set3 & Set2)) - (Set1 & Set2 & Set3)
print(new_set)
print("\n")

#(d) : Create a new set of all integers in the range 1 to 10 that are not in Set1.
print("(d)")
new_set1 = {1,2,3,4,5,6,7,8,9,10}
new_set = new_set1 - Set1
print(new_set)
print("\n")

#(e) : Create a new set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3.
print("(e)")
new_set = new_set1 - (Set1|Set2|Set3)
print(new_set)
print("\n")

