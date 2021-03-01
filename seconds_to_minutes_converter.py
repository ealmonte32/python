#ealmonte32
# we want to check how many minutes in the number of seconds entered

print("\nSeconds to minutes converter.\n")

# we ask user to enter the number of seconds
totalseconds = int(input("Enter the number of seconds: "))
check_minutes = int(totalseconds / 60)
seconds_remainder = (totalseconds % 60)

# this format is called python's implied line continuation
# so that when you write it out instead of being one long line
# you can just write everything into multiple lines more clear
print("There are", \
      check_minutes, "minutes and", \
      seconds_remainder, "seconds in", \
      totalseconds, "seconds.")

"""
to explain the abobe solution:
i simply take in the total number in seconds
then i check how many minutes are in those total seconds by dividing by 60
then we know that if there are any remainder it will be because they are
less than 60 seconds, so we want to save these as seconds_remainder
when we do the seconds remainder calculation we use the modulo operator
by using the modulo we only get the result of the remainder, which is what we want
when there are seconds that did not reach 60, and we add these remainders to final
result..
one important note here is that if you dont add the specific integer type for
the check_minutes variable, you might get a decimal number such as 1.08833
and we cannot have this to explain minutes, we need whole numbers, so this is
why you tell it that totalseconds will be an integer, thus giving check_minutes
the result in non-decimal format
"""
