# Make a while loop that runs until start is falsey.
# Inside the loop, use random.randint(1, 99) to get a random number between 1 and 99.
# If that random number is even (use even_odd to find out), print "{} is even", putting the random number in the hole. Otherwise, print "{} is odd", again using the random number.
# Finally, decrement start by 1.

import random

def even_odd(num):
    # If % 2 is 0, the number is even.
    # Since 0 is falsey, we have to invert it with not.
    return not num % 2

start = 5

while True:
  rand_number = random.randint(1,99)
  if start == 0:
    break;
  elif even_odd(rand_number):
    print("{} is even".format(rand_number))
  else:
    print("{} is odd".format(rand_number))
  start-=1
