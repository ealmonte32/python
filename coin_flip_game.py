# ealmonte32
# coin flip game with money balance

import sys
import random

# this would be our initial money balance of 5 dollars
balance = int(5)

print("\n**************************************")
print("\nGAME TITLE: Coin Flip Casino! - $1 per play")
print("Guess whether the coin will land on heads or tails.")
print("You have a balance of $" + str(balance) + " dollars.")
# the reason for converting the balance to a string is because
# if we want to concatenate we use the + sign but the variables need to be
# of the same type, so the words are strings, while the balance is originally
# an integer as we assigned it up there, so if we want to simply display it
# inside a print statement, we must convert it to a string just to display it


# we begin the game by running a while loop that continues until you run out of money
# notice we have to indent after the while loop and then after the if statement..

# we let the player know what the possible typed answers are
print("\nAcceptable answers are: head, heads, tail, tails, or stop to exit the game.")

while balance > 0:
    print("\nThe dealer just flipped a coin, guess the outcome!\n")
    answer = input("Type your answer and press enter: ")

    # a way to compare the typed anwser to a string is to put ' ' around the word
    # we assign the word head/heads to equal the number 1 and tail/tails to 2
    if answer == 'heads' or answer == 'head':
        answer = 1
    if answer == 'tails' or answer == 'tail':
        answer = 2
    if answer == 'stop':
        break

    # now we are assigning a value to the answer based on comparison
    # this below assigns the variable coin a random number (integer) from 1 to 2
    # since a coin has two sides, I simply make heads=1 and tails=2 (shown above)
    coin = random.randint(1,2) # this line executes the "coin flip"

    if coin == 1:
        print("The coin landed on heads.")
    if coin == 2:
        print("The coin landed on tails.")

    # this is where we compare the result of the random integer that was assigned to coin
    # to the answer that you typed in
    if answer == coin:
        print("Congratulations, you win!\n")
        balance = balance + 1
        print("Your current money balance is: $" + str(balance))
    else:
        print("Sorry, you lose =[\n")
        balance = balance - 1
        print("Your current money balance is: $" + str(balance))

