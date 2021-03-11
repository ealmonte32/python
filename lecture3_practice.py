#ealmonte32
#CSIT104 - Lecture 3 Practice

import time

def radius_checker():
    print("You selected: Radius Checker.\n")
    radius = float(input("Enter the radius: "))

    if (radius <= 0):
        print("(Error)",radius,"is not a valid radius, program will now exit.")
    else:
        area = (radius * radius * 3.14159)
        print("The area for a circle with a radius of",radius,"is",area)
    time.sleep(2)
    main()


def posneg_checker():
    print("You selected: Positive or Negative Number Checker.\n")
    num_check = float(input("Enter a number to check if it is positive: "))

    if (num_check > 0):
        print("That's a Positive number.")
    elif (num_check == 0):
        print("That's a neutral number =]")
    else:
        print("That's a Negative number.")
    time.sleep(2)
    main()
    

def odd_even_checker():
    print("You selected: Odd or Even Number Checker.\n")
    num_input = int(input("Enter a whole number (an integer): "))

    # using modulo operator, we divide by 2 and check for remainder
    check_even = (num_input % 2)

    # this says if the remainder does not equal 0, then it is not divisible by 2
    # and if it is not divisible by 2, then it is an odd number
    if check_even != 0:
        print(num_input, "is Odd.")
    else:
        print(num_input, "is Even.")
    time.sleep(2)
    main()
    

def grading_checker():

    print("You selected: Final Grade Checker.\n")
    score = float(input("Enter the final score: "))

    #we check the entered score (decimal number), and give corresponding letter grade
    if (score >= 90.0):
        print("Grade: A")
    
    elif (score >= 80.0):
        print("Grade: B")
    
    elif (score >= 70.0):
        print("Grade: C")
    
    elif (score >= 60.0):
        print("Grade: D")

    else:
        print("Grade: F")
    time.sleep(2)
    main()
    

def temp_checker():
    print("You selected: Temperature Checker.\n")
    temp = float(input("Enter the temperature in Fahrenheit: "))

    #we check the entered temp number (decimal), and give corresponding result
    if (temp > 99):
        print("Temperature is Too Hot!")
    
    elif (temp < 40):
        print("Temperature is Too Cold!")
    
    else:
        print("Temperature is Just Right.")
    time.sleep(2)
    main()
    

def main():

    print("\n-----------------------------------------")
    print("CSIT 104 - LECTURE 3 PYTHON PRACTICE\n")
    print("Available Programs to choose:\n")
    print(" (1)Radius Checker \
            \n (2)Positive/Negative Checker \
            \n (3)Odd/Even Checker \
            \n (4)Grade Checker \
            \n (5)Temperature Checker \
            \n\n (0)Exit\n")

    # to prevent ValueError exception, I dont use int() for program variable
    program = input("Enter the number corresponding to the program and press enter: ")
    
    if (program == "1"):
        radius_checker()
            
    elif (program == "2"):
        posneg_checker()
        
    elif (program == "3"):
        odd_even_checker()
        
    elif (program == "4"):
        grading_checker()

    elif (program == "5"):
        temp_checker()

    elif (program == "0"):
        print("Program Exited.")
        exit

    else:
        print("Error: You did not enter a valid number, please try again.")
        time.sleep(2)
        main()


#main function initializes
if __name__ == "__main__":
    main()


"""
this comment block is for lecture reference purposes only


print(radius > 0)
this code above will print out True or False depending on the evaluation it concludes
the inside of the parentheses is what you are evaluating
so if radius is greater than 0, it will be True, thus printing True
but if the radius is not greater than 0, it will print False

    
#this simply means a manual assignment of True to the variable lightsOn
lightsOn = True

#this will print out the current value of lightsOn
print(lightsOn)

#this prints out the integer value of True
print(int(True))

#this was added by me just to show the opposite of True in integer
print(int(False))

#this returns False because any empty value will be false
print(bool(0))
        
#these would return False because after evaluating the inside of the parentheses
b = (1 > 2)
print(b)
"""
