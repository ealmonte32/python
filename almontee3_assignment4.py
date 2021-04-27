#ealmonte32
#CSIT104 - Assignment 4

# Program 1
print("\n Program #1")
print("----------------------------")
print("Adding odd numbers from 1 to 100, print final sum.")
oddtotalsum = 0
for i in range(1,101,2):
  oddtotalsum = oddtotalsum + i
print("Total sum of all odd numbers:", oddtotalsum)

# add space between programs for cleaner view
print("\n")

# Program 2
print("\n Program #2")
print("----------------------------")
print("Print a pattern using nested loop.")
i = 1
while i <= 6:
  innerloop = 1
  for j in range(1, i+1):
    print("*", end="")
    innerloop += 1
  print()
  i += 1

# add space between programs for cleaner view
print("\n")

# Program 3
print("\n Program #3")
print("----------------------------")
print("Print a two dimensional table using nested loop.")
i = 1
while i <= 5:
  for j in range(1, 6):
    print(j, end=" ")
  print()
  i += 1

# add space between programs for cleaner view
print("\n")


# Program 4
print("\n Program #4")
print("----------------------------")
print("Ask user for favorite novel and sentence, then display in different formatting.\n")
novel = input("What is your favorite novel? ")
sentence = input("Write a sentence about anything: ")
print("\n")
print("Your favorite novel in UPPER:",novel.upper())
print("Your favorite novel in lower:",novel.lower())
print("\n")
print("The result of your sentence after replacing \"e\" with \"&\":", sentence.replace("e", "&"))

