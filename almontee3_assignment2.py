#ealmonte32
#CSIT104 - Assignment 1

#Program 1
print("==================================================")
print("\nProgram 1:\nCheck if a given number is divisible by 3 or 5 or neither.\n")

number = int(input("Enter a number: "))
if (number % 3 == 0) and (number % 5 == 0):
    print(number,"is divisible by 3 and 5.")
elif (number % 3 == 0):
    print(number,"is divisible by 3.")
elif (number % 5 == 0):
    print(number,"is divisible by 5.")
else:
    print(number,"is not divisible by 3 or 5.")



#Program 2
print("==================================================")
print("\nProgram 2:\nCheck how many digits a given number is.\n")

number = int(input("Enter a number: "))
print(number, "is a", len(str(abs(number))), "digit number.")
