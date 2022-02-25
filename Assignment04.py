# QUESTION1 : To solve the problem of Tower of Hanoi with three disks.

print("Printing Tower Of Hanoi with three disks:\n")
def Tower_of_Hanoi(n , from_rod, to_rod, mid_rod):
	if n == 0:
		return

	Tower_of_Hanoi(n-1, from_rod, mid_rod, to_rod)
	print(f"Move disk {n} from rod {from_rod} to rod {to_rod}.")
	Tower_of_Hanoi(n-1, mid_rod, to_rod, from_rod)

# calling funtion for 3 disks
Tower_of_Hanoi(3, 'A', 'C', 'B')
print("\n\n")


# QUESTION2 : To print the Pascal's triangle for n number of rows both Recursive and Iterative procedures.

#Input the number of rows.
n = int(input("Enter the number of rows in the Pascal's Triangle:\n"))

#Using Recursion Procedure.

print("\nUsing Recursion Procedure:\n")
def pascal_triangle(n, original_length = n):
    if n == 0:
        return

    pascal_triangle(n-1, original_length)

    #Printing the spaces
    print('  ' * (original_length - n), end = '')

    #First number is always 1
    entry = 1
    for i in range(1, n + 1):

        print(entry, end = '   ')

        #Using Binomial Coefficient
        entry = entry * (n - i) // i
    print()
pascal_triangle(n)

#Using Iterative Procedure.

print("\nUsing Iterative Procedure:\n")
for line in range(1, n+1):

    print('  ' * (n - line), end = ' ') # For Spacing

    x = 1
    for i in range(1, line+1):

        print(x, end = '   ')

        x = x * (line - i) // i
    print() # For New Line

print("\n\n")


# QUESTION 3 :

num1, num2 = map(int,input("Enter two integer values:\n").split())
quotient = num1 // num2
remainder = num1 % num2

print("\n(a)")

print("Check whether the quotient is callable or not?\n", callable(quotient))
print("Check whether the remainder is callable or not?\n", callable(remainder))

print("\n(b)")

print("Check whether all the values are non zeros or not?")

if (quotient == 0):
    print(" No, only the quotient is zero.")
if (remainder == 0):
    print("No, only the remainder is zero")
if (quotient != 0 and remainder != 0):
    print("Yes, all the values are non zeros.")

print("\n(c)")
new_list = [quotient + 4, remainder + 4, remainder + 5, quotient + 5, remainder + 5, quotient + 6, remainder + 6]

result = []
for i in range(len(new_list )):
    if new_list [i] > 4:
        result.append(new_list [i])
print(f"Filtered out the values which are greater than 4:\n {result} ")

print("\n(d)")
set_result = set(result)
print("Set:\n",set_result)

print("\n(e)")
immutable_set = frozenset(set_result) #frozenset is used to make the set immutable.
print("Immutable set:\n", immutable_set)

print("\n(f)")
print("Hash value of the maximum value from the set:\n", hash(max(immutable_set)))
print("\n\n")


# QUESTION 4:

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def __del__(self):
        print("Object destruction.")

# Creating object
student1 = Student("Nikita Sharma", 21103002)
print("Object creation.")

print(f"The name of the student is {student1.name} and roll number is {student1.roll_number}.")

# Deleting object
del student1
print("\n\n")


# QUESTION 5:

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

#Creating Employee Records
employee_1 = Employee("Mehak", 40000)
employee_2 = Employee("Ashok", 50000)
employee_3 = Employee("Viren", 60000)

#(a) Updating the salary of Mehak to 70000
employee_1.salary = 70000
print(f"(a) The updated salary of {employee_1.name} is {employee_1.salary}.")

#(b) Deleting the record of employee Viren
print("(b) Record of the employee Viren deleted.", end='')
del employee_3
print("\n\n")


# QUESTION 6:

# Inputting a word from the first friend i.e. George
word = input("Enter the word:\n")
word = word.lower()

# Inputting a new meaningful word using the exact same letters.
test_word = input("Enter a new meaningful word using the exact same letters to test your friendship:\n")
test_word = test_word.lower()

# Defining a Dictionary
def count_dict(word):
    count = {}
    list1 = list(word)

    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

# Shopkeeper's Input to verify the word's meaning.
def shopkeeper_input():
    if count_dict(word) != count_dict(test_word):
        print("The letters aren't exact.\nTHEIR FRIENDSHIP IS A FAKE..")
        return
    answer = input("Check whether the new word is meaningful or not? (y/Y or n/N )\n")

    if answer == 'y' or answer == 'Y':
        print("THEIR FRIENDSHIP IS A REAL.")
    elif answer == 'n' or answer == 'N':
        print("The word doesn't have a meaning.\nTHEIR FRIENDSHIP IS A FAKE.")
    else:
        print("Invalid Input\n Try Again.")
        shopkeeper_input()

shopkeeper_input()