# make a list to hold onto items
shopping_list = []

def show_help():
  # print out instructions on how to use the app
  print("What should we pick up from the store?")
  print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help message.
Enter 'SHOW' to see your current list.
""")

def show_list():
  # print out the list
  print("Here's your list:")

  for item in shopping_list:
    print(item)

def add_to_list(new_item):
  shopping_list.append(new_item)
  print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

show_help()

while True:
  # ask for new items
  new_item = input("> ")

  #be able to quit the app
  if new_item.lower() == "done":
    break

  # have a HELP command
  elif new_item.lower() == 'help':
    show_help()
    continue

  # have a SHOW command
  elif new_item.lower() == 'show':
      show_list()
      continue

  add_to_list(new_item)

show_list()
