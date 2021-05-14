#ealmonte32

import datetime # this is just for displaying the date and time

# this date_variable means that whenever you call it, it will run
# the command that it is equal to
date_variable = datetime.datetime.now()

# we want to stop the program when user makes a specific choice
# so we make a variable and we only call it when we are ready to
# stop the program, so the while loop down there always runs unless
# the stop_program variable is changed to anything other than 0
stop_program = 0

# just some empty lists to fill up
list_of_students = []
list_of_faculty = []

def student_function(variable1, variable2, variable3):
  # these things that are under the function happen only when you call the function
  # and give it the 3 variables it requires to run, the append for list goes inside
  # the brackets because we want all three variables to be part of the same entry on the list
  list_of_students.append([variable1, variable2, variable3])
  print() # add blank line

def faculty_function(variable1, variable2):
  list_of_faculty.append([variable1, variable2])
  print() # add blank line

def print_users_info():
  total_students = len(list_of_students)
  total_faculty = len(list_of_faculty)

  print("----- STUDENTS -----")
  for i in range(0, total_students):
    print("Student ID: ", list_of_students[i][0])
    print("Student Name: ", list_of_students[i][1])
    print("Major: ", list_of_students[i][2])
    print() # add blank line

  print("----- FACULTY -----")
  for i in range(0, total_faculty):
    print("Faculty Name: ", list_of_faculty[i][0])
    print("Faculty Job Description: ", list_of_faculty[i][1])
    print() # add blank line


# now we run the loop to run the program
while stop_program == 0:
  print("University Users Management:\n")
  print(date_variable)
  print("Enter (1) for Student Input")
  print("Enter (2) for Teacher Input")
  print("Enter (3) to Print Users info")
  print("Enter (0) to Exit")
  choice = int(input(" Choice: "))
  
  if choice == 0:
    print("Good bye.")
    stop_program = 1 # stops the program
    
  elif choice == 1:
    student_name = input("Enter the student name: ")
    student_id = int(input("Enter the student ID number: "))
    student_major = input("Enter the student major: ")

    # we now call the student function so that it takes all our input
    # and does whatever is programmed to do inside the function with it
    # if you see the variable names being sent, i am purposely using
    # the student_id in the first variable input because i know that
    # when it goes to the student function, the first variable is being
    # used as the student ID entry..
    student_function(student_id, student_name, student_major)
    print(" ..sending info to student list.. done.")
    print() # add blank line
    
  elif choice == 2:
    faculty_name = input("Enter faculty name: ")
    faculty_job = input("Enter faculty job description: ")
    faculty_function(faculty_name, faculty_job)
    print("..sending info to faculty list.. done")
    print() # add blank line
    
  elif choice == 3:
    print() # add blank line
    print_users_info()
    
  else:
    print("Error, incorrect option entered.")
