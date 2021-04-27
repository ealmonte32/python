#ealmonte32
#CSIT104 - Assignment 3

# Program 1
print("\n Program #1")
print("Maximum and Minimum number finder.")
print("Please enter three numbers to begin.\n")
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
third_num = int(input("Enter the third number: "))

#find max
if (first_num >= second_num) and (first_num >= third_num):
  max_num = first_num
elif (second_num >= first_num) and (second_num >= third_num):
  max_num = second_num
else:
  max_num = third_num

#find min
if (first_num <= second_num) and (first_num <= third_num):
  min_num = first_num
elif (second_num <= first_num) and (second_num <= third_num):
  min_num = second_num
else:
  min_num = third_num

print("\nHere are your results.")
print("Maximum number is:",max_num)
print("Minimum number is:",min_num)

print("--------------------------")
# Program 2
print("\n Program #2")
print("Total String length finder.")
print("Please enter two strings to begin.\n")
input_one = input("Enter first String: ")
input_two = input("Enter second String: ")
total_string = (input_one + input_two)
print("The final String is:",input_one + input_two)
print("The length of the final String is:",len(total_string))
