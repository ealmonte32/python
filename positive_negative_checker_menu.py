#ealmonte32
#CSIT 104 - In Class Programming Q2

def check_neg(numbers_list):
    all_negs = []
    for negative in numbers_list:
        if negative < 0:
            all_negs.append(negative)
    return all_negs

def check_pos(numbers_list):
    all_pos = []
    for positive in numbers_list:
        if positive > 0:
            all_pos.append(positive)
    return all_pos

def main():
    numbers_list = [-1,2,-3,4,-5,6,-7,8,9,10,-11]

    print("\n-----------------------------------------")
    print("Positive or Negative Number Checker Program\n")
    print("Available functions to choose:\n")
    print(" (a) Check Negative \
            \n (b) Check Positive \
            \n (c) Quit\n")

    choice = input("Type the letter corresponding to the program and press enter: ")
    
    if choice not in ("a","b","c"):
        print("\n (Error): You entered an incorrect letter as choice. Please try again.")
        main()
    
    if (choice == "a"):
        print("Negative numbers in list are:",check_neg(numbers_list))
        
    elif (choice == "b"):
        print("Positive numbers in list are:",check_pos(numbers_list))
            
    elif (choice == "c"):
        print(numbers_list)
        exit()

#main function initializes
main()
