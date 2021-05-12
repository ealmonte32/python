#ealmonte32

users_list = []

def add_user(username):
  if username in users_list:
    print("That user already exists")
  else:
    users_list.append(username)

def del_user(username):
  if username in users_list:
    users_list.remove(username)
  else:
    print("Sorry, that user was not found")

def main():
  print()
  print("  Menu options:")
  print("1. See current list of users")
  print("2. Add a user")
  print("3. Remove a user")
  choice = int(input("\nEnter number of option: "))

  if choice == 1:
    if len(users_list) == 0:
      print("\nNo users\n")
    else:
      line = 1
      for i in users_list:
        print(line,":",i)
        line += 1
    main()
  elif choice == 2:
    username = input("\nEnter name of user to add and press enter: ")
    add_user(username)
    print()
    main()
  elif choice == 3:
    username = input("\nEnter name of user to delete and press enter: ")
    del_user(username)
    main()

main()
