#ealmonte32

print("==================================================")
print("\nProgram:\nCheck if a given number is divisible by 3 or 5 or neither.\n")

number = int(input("Enter a number: "))
if (number % 3 == 0) and (number % 5 == 0):
    print(number,"is divisible by 3 and 5.")
elif (number % 3 == 0):
    print(number,"is divisible by 3.")
elif (number % 5 == 0):
    print(number,"is divisible by 5.")
else:
    print(number,"is not divisible by 3 or 5.")