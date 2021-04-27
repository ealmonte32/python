#ealmonte32
#CSIT104 - lecture 5 exercises

checknum = 0
alldivnumbersadded = 0
while (checknum <=100):
  if checknum % 5 == 0:
    print(checknum)
    alldivnumbersadded += checknum
  checknum += 1
print("")
print("All numbers divisible by 5 total:",alldivnumbersadded)

print("----------------------------------")
print("Largest entered number checker.")
stopprog = 0
while stopprog != 1:
  num1 = int(input("Enter 1st number: "))
  num2 = int(input("Enter 2nd number: "))
  num3 = int(input("Enter 3rd number: "))
  num4 = int(input("Enter 4th number: "))
  num5 = int(input("Enter 5th number: "))
  if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5:
    largest = num1
  elif num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5:
    largest = num2
  elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5:
    largest = num3
  elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5:
    largest = num4
  else:
    largest = num5
  print("The largest number entered was:", largest)
  asktocontinue = input("Would you like to continue this program? (y/n)")
  if asktocontinue == "n":
    stopprog = 1
    
    
    
#slide 28 exercise

i = 1
sum = 0
while sum < 100:
  sum = sum + i
  i += 1
  print("sum:",sum,"i:",i)

print("-- convert the while loop into similar for loop --")

x = 1
sum = 0
for sum in range(100):
  sum = sum + x
  x += 1
  print("sum:", sum, "x:", x)
  if sum >=100:
    break

#slide 29
for i in range(1,5):
  j = 0
  while j < i:
    print("i is currently:", i)
    print("j is currently:", j) #, end = " ")
    print(" ")
    j += 1


#slide 31
i = 1
while i <= 5:
    num = 1
    for j in range(1, i + 1): 
        print(num, end = "G")
        num += 2
    print(" test ")
    i += 1


#slide 34 practice problems
print("print all from 0 to 6 except 3 and 6:")
for i in range(7): #loops from 0 to 6, does not include 7
  if i == 3 or i == 6:
    continue #this just means if i is ever 3 or 6, just continue
  else: #adding this here to otherwise print the value of i
    print(i)




print("\n-------------\n")
print("pattern with nested loop number:")

i = 1
while i <= 6:
  for j in range(1, i): #changing the i to make range 1,7 ruins it
    print(i, end = "") #print current i loop number without new line and print it j many times
  print(i) #print the i loop number after the j loop
  i += 1 #increase the i loop to reach 6
