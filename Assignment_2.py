# Question 1: Write Python code for the following:

input_string = "Python is a case sensitive language"
print(input_string)
# (a) Find the length of the input string.
print('\n (a)')
print("The length of the input string: \n",len(input_string))

# (b) Reverse the order of the string in one line code.
print('\n (b)')
print("Reverse of the given input string: \n",input_string[ : :-1])

# (c) Using Slice function store "a case sensitive" in new string.
print('\n (c)')
new_string = input_string[10:26]
print("Store 'a case sensitive' in new string: \n ",new_string)

# (d) Replace "a case sensitive" with "object oriented".
print('\n (d)')
updated_string = input_string.replace("a case sensitive","object oriented")
print("Updated string after replacing 'a case sensitive' with 'object oriented': \n",updated_string)

# (e) Find index of substring "a" in the given input string.
print('\n (e)')
index_substring = input_string.find('a')
print("The index of substring 'a' in the given input string: \n",index_substring)

# (f) Remove the white spaces from the given input string.
print('\n (f)')
inp_string = input_string.replace(' ', '')
print("String after removing the white spaces from the given input string: \n",inp_string)


# Question 2: Use the string formatting to print your name, SID, department name and CGPA in the following output:

name = "Nikita Sharma"
SID = 21103002
department_name = "CSE"
CGPA = 9.9
print(f"\nHey, {name} Here!\n"
      f"My SID is {SID} \n"
      f"I am from {department_name} department and my CGPA is {CGPA}")


# Question 3: For a = 56 and b = 10 with the help of bitwise operators calculate the following:

a = 56
b = 10
print('\n (a)')
print("With the help of bitwise AND operator:\n",a & b)
print('\n (b)')
print("With the help of bitwise OR operator:\n",a | b)
print('\n (c)')
print("With the help of bitwise XOR operator:\n",a ^ b)
print('\n (d)')
print("Bitwise Left shift a with 2 bits: \n",a << 2)
print("Bitwise Left shift b with 2 bits: \n",b << 2)
print('\n (e)')
print("Bitwise Right shift a with 4 bits: \n",a >> 4)
print("Bitwise Right shift b with 4 bits: \n",b >> 4)


# Qusetion 4: To find the greatest of three numbers entered by the user.

num1 = float(input("\nEnter the first number:\n"))
num2 = float(input("Enter the second number:\n"))
num3 = float(input("Enter the third number:\n"))

if(num1 > num2) and (num1 > num3):
    print(f"First number i.e. {num1} is the greatest.")
elif (num2 > num1) and (num2 > num3):
    print(f"Second number i.e. {num2} is the greatest.")
else:
    print(f"Third number i.e. {num3} is the greatest.")


# Question 5: To check if the word 'name' is present in the string entered by the user or not(Print: "Yes" or "No").

input_string = input("\nEnter the string:\n")
print("\nThe word 'name' is present in the entered string or not (Yes or No)?")

if "name" in input_string:
    print("Yes \n")
else:
    print("No \n")


# Question 6: To check whether the given input lengths can form a triangle or not(Print: "Yes" or "No").

side1 = int(input("Enter the first side of a triangle:\n"))
side2 = int(input("Enter the second side of a triangle:\n"))
side3 = int(input("Enter the third side of a triangle:\n"))
print("\nThe given input lengths can form a triangle or not (Yes or No)?")

if ((side1+side2) > side3 and (side2+side3) > side1 and (side3+side1) > side2 and side1 > 0 and side2 > 0 and side3 > 0):
    print("Yes")
else:
    print("No")



