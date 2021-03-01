#ealmonte32

# ask to enter a number
print("\nOdd or Even number checker.\n")
num_input = int(input("Enter a number: "))

# using modulo operator, we divide by 2 and check for remainder
check_even = (num_input % 2)

# this says if the remainder does not equal 0, then it is not divisible by 2
# and if it is not divisible by 2, then it is an odd number
if check_even != 0:
    print(num_input, "is Odd.")
else:
    print(num_input, "is Even.")


"""
simple example of printing all odd numbers from 1 to 10
for number in range(1, 10):
    if(number % 2 != 0):
        print(number)
"""
