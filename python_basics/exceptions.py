
def count():
try:
  count = int(input("Give me a number: "))
except ValueError:
  print("That's not a number!")
else:
  print("Hi " * count)


def add(a, b):
  try:
    return float(a) + float(b)
  except ValueError:
    return None
  else:
    return float(a) + float(b)
