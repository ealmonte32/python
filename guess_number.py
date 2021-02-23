#import the random module
import random

a = random.randint(1,10)

b = int(input("Guess a number between 1 and 10, enter it here: "))

if a == b:
    print("congratulations, you win!")
else:
    print("sorry, you lose =[")

#this will put spaces after each comma
print("The numbers were:", a,"and", b)

#if you want to control the commas after each output without explicit spaces
print("The numbers were: " + str(a) + " and " + str(b))

#it is obviously better to print the answers in int raw format values
#than having to convert to string to print as the last code line shows..