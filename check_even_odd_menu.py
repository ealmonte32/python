#ealmonte32
#CSIT 104 - In Class Programming Q3

def check_even(numbers_list):
    all_even = []
    for even in numbers_list:
        if even % 2 == 0:
            all_even.append(even)
    return all_even

def check_odd(numbers_list):
    all_odd = []
    for odd in numbers_list:
        if odd % 2 != 0:
            all_odd.append(odd)
    return all_odd

def main():
    numbers_list = [-1,2,-3,4,-5,6,-7,8,9,10,-11]

    print("\n-----------------------------------------")
    print("Even or Odd Number Checker Program\n")
    print("Available functions to choose:\n")
    print(" (a) Check Even \
            \n (b) Check Odd \
            \n (c) Quit\n")

    choice = input("Type the letter corresponding to the program and press enter: ")
    
    if choice not in ("a","b","c"):
        print("\n (Error): You entered an incorrect letter as choice. Please try again.")
        main()
    
    if (choice == "a"):
        print("Even numbers in list are:",check_even(numbers_list))
        
    elif (choice == "b"):
        print("Odd numbers in list are:",check_odd(numbers_list))
            
    elif (choice == "c"):
        print(numbers_list)
        exit()

#main function initializes
main()
