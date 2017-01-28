import os

# make a list to hold onto items
shopping_list = []

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear') # if windows ('nt') run cls, otherwise run clear (because probably Linux of Mac)

def show_help():
  clear_screen()
  # print out instructions on how to use the app
  print('What should we pick up from the store?')
  print('''
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help message.
Enter 'SHOW' to see your current list.
''')

def add_to_list(new_item):
  show_list()
  if len(shopping_list):
    position = input('Where should I add {}?\n'
                      'Press ENTER to add to the end of the list\n'
                      '> '.format(new_item))
  else:
    position = 0

  try:
    position = abs(int(position))
  except ValueError:
    position = None
  if position is not None:
    shopping_list.insert(position-1, new_item)
  else:
    shopping_list.append(new_item)
  show_list()


def show_list():
  clear_screen()
  # print out the list
  print('Here\'s your list:')

  index = 1
  for item in shopping_list:
    print('{}. {}'.format(index, item))
    index += 1

  print('-' * 10)

show_help()

while True:
  # ask for new items
  new_item = input('> ')

  #be able to quit the app
  if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
    break

  # have a HELP command
  elif new_item.upper() == 'HELP':
    show_help()
    continue

  # have a SHOW command
  elif new_item.upper() == 'SHOW':
      show_list()
      continue
  else:
    add_to_list(new_item)

show_list()
