"cheese" in "cheeseshop" # True
"cheese" in [] # False

# Example 1
days_open = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
today = "Tuesday"

if today in days_open:
  print("Come on in!")
else
  print("Sorry, we are closed")

# or

if today not in days_open
  print("Sorry, we are closed")
else
  print("Come on in!")

# Example 2
time = 15
store_open = None
store_hours = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

if time in store_hours:
    store_open = True
else:
    store_open = False
