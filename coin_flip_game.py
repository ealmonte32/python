# ealmonte32
# coin flip game with money balance

import sys
import random
import time


# we have to define a function that draws on the screen the coin/quarter
# so that when the coin gets flipped and lands for example as heads
# the heads function gets called and prints out exactly what you write inside it
# below are both functions for heads and tails which we can then call later on

def coin_heads():
    print(
'''
        _.-'~~`~~'-._
     . `  B   E   R  `.
    / I               T '
  /`       .-'~"-.       `\\
 ; L      / `-    \      Y ;
|        />  `.  -.|        |
|       /_     '@-._)       |
|        |-  _.' \ |        |
;        `~~;     \\\\        ;
 ;          /      \\\\))    ;
  \        '.___.-'`"     /
   `\                   /`
     '._   H E A D S _.'
        `'-..,,,..-'`

'''
)

def coin_tails():
    print(
'''
        _.-'~~`~~'-._
     .` T E D   S T A`.
    / I               T`\\
  /`N        <@)        E \\
 ; U   /-\___/ \___/-\   S ;
|     //             \\\\     |
|   ////  \       /  \\\\\\\\   |
|  ||||||           ||||||  |
;   \   | \__{|}___/ |  /   ;
 ;   ` /     /|\      \\'   ;
  \        ~~~~~~~        /
   `\                   /`
     '. T  A  I  L  S .'
        `'-..,,,..-'`

'''
)


# now we need to make a function that shows a coin being flipped in the air
# so we make something that changes every millisecond from a circle to a line
# just like what a coin being flipped in the air looks like

# msg is what we want to display when we call this function
# n_chars means how many characters we want to see at the same time displayed
# i chose 1 because it makes it look like the coin was flipped in the air as it moves
def scrolling_coin_flip(msg, n_chars):
    len_msg = len(msg) #the length of the message is equal to total letters we write ex: OO00||
    counter = 0
    while counter < 25: #the 25 just means how many characters we want to show during flip
        displayed = ""

        #this is a "for" loop
        for loop in range(n_chars):
            displayed += msg[(counter+loop)%len_msg]
        print(f"\n{displayed}", end="")
        time.sleep(0.04) #the time before each letter shows
        counter = (counter + 1) #we increase the counter during every loop so it gets to 25
    return


# this would be our initial money balance of 5 dollars
balance = int(5)

print("\n***************************************")
print("\n GAME: Coin Flip Casino! - $1 per play")
print(" Guess whether the coin will land on heads or tails.")
print(" You have a balance of $" + str(balance) + " dollars.")
# the reason for converting the balance to a string is because
# if we want to concatenate we use the + sign but the variables need to be
# of the same type, so the words are strings, while the balance is originally
# an integer as we assigned it up there, so if we want to simply display it
# inside a print statement, we must convert it to a string just to display it


# we begin the game by running a while loop that continues until you run out of money
# notice we have to indent after the while loop and then after the if statement..

while balance > 0:
    print("\n\nThe dealer is about to flip a coin, guess the outcome!")
    
    # we let the player know what the possible typed answers are
    print("\nAcceptable answers are: head, heads, tail, tails, or stop to exit the game.")
    answer = input("Type your answer and press enter: ")

    # a way to compare the typed anwser to a string is to put ' ' around the word
    # we assign the word head/heads to equal the number 1 and tail/tails to 2
    if answer == 'heads' or answer == 'head':
        answer = 1
    elif answer == 'tails' or answer == 'tail':
        answer = 2
    elif answer == 'stop':
        break
    else:
        # if none of the conditions above are met, we know the user did not enter one
        # of the accepted answers, so we restart the loop again after waiting 2.5 seconds
        print("\n (Error: you did not enter an acceptable answer, please try again..)")
        time.sleep(2.5)
        continue


    # now we are assigning a value to the answer based on comparison
    # this below assigns the variable coin a random number (integer) from 1 to 2
    # since a coin has two sides, I simply make heads=1 and tails=2 (shown above)
    coin = random.randint(1,2) # this line executes the "coin flip"
    scrolling_coin_flip("OO00||00OO", 1)

    if coin == 1:
        print("\n The coin landed on heads.")
        coin_heads()
    if coin == 2:
        print("\n The coin landed on tails.")
        coin_tails()

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
