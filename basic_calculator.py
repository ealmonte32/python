#ealmonte32

def add(x,y):
    return (x + y)

def subtract(x,y):
    return (x - y)

def multiply(x,y):
    return (x * y)

def divide(x,y):
    return (x / y)

def main():

    print("\n-----------------------------------------")
    print("PYTHON CALCULATOR\n")
    print("Available functions to choose:\n")
    print(" (1) Add \
            \n (2) Subtract \
            \n (3) Multiply \
            \n (4) Division \
            \n\n (0) Quit\n")

    choice = int(input("Enter the number corresponding to the program and press enter: "))
    
    if choice not in (0,1,2,3,4):
        print("\n (Error): You entered an incorrect number as choice. Please try again.")
        main()
        
    if (choice == 0):
        print("Program Quit.")
        exit()

    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    
    if (choice == 1):
        print("Result is",add(x,y))
        main()
            
    elif (choice == 2):
        print("Result is",subtract(x,y))
        main()
        
    elif (choice == 3):
        print("Result is",multiply(x,y))
        main()
        
    elif (choice == 4):
        print("Result is",divide(x,y))
        main()

#main function initializes
main()
