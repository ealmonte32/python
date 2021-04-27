#ealmonte32
#CSIT104 - Assignment 5

# Program 1
print("\n Program #1 (take two strings as parameters)")
print("----------------------------------------------")
def fullname(fname, lname):
  print("Your Full Name is: ",fname,lname)
string1 = input("Enter First Name: ")
string2 = input("Enter Last Name: ")
fullname(string1, string2)

# add space between programs for cleaner view
print("\n")

# Program 2
print("\n Program #2 (bigger value from function)")
print("-------------------------------------------")
def bigger(x, y):
  print("The bigger value is: ",max(x,y))
  """
  if you dont want built-in function then you simply do this below
  if x > y:
    biggervalue = x
  else:
    biggervalue = y
  print("The bigger value is: ",biggervalue)
  """
inputx = input("Enter value for X: ")
inputy = input("Enter value for Y: ")
bigger(inputx,inputy)


# add space between programs for cleaner view
print("\n")

# Program 3
print("\n Program #3 (summation of integer values)")
print("--------------------------------------------")
def summation(int_a, int_b):
  total = int_a + int_b
  print(total)

default_a = 10
default_b = 20

user_input_a = int(input("Enter value for integer 'a': "))
user_input_b = int(input("Enter value for integer 'b': "))

print("Case A - Parameters are user specified.")
case_a = summation(user_input_a, user_input_b)

print("Case B - Parameters are default.")
case_b = summation(default_a, default_b)

print("Case C - Parameter 'a' is default, and 'b' is user specified.")
case_c = summation(default_a, user_input_b)


# add space between programs for cleaner view
print("\n")


# Program 4
print("\n Program #4 (add even numbers between 1 and 100)")
print("---------------------------------------------------")
#using continue statement
totaleven = 0
checknum = 0
for i in range(101):
  checknum += 1
  if checknum % 2 != 0:
    continue
  else:
    totaleven = totaleven + checknum
print("Sum of all even numbers between 1 and 100: ",totaleven)

"""
#Not using unnecessary continue statement
totaleven = 0
checknum = 0
for i in range(101):
  if checknum % 2 == 0:
    totaleven = totaleven + checknum
  checknum += 1
print("Sum of all even numbers between 1 and 100: ",totaleven)
"""
