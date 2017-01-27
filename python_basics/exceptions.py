# Example 1
def count():
  try:
    count = int(input("Give me a number: "))
  except ValueError:
    print("That's not a number!")
  else:
    print("Hi " * count)

# Example 2
def add(a, b):
  try:
    return float(a) + float(b)
  except ValueError:
    return None
  else:
    return float(a) + float(b)

# EXAMPLE 3
def squared (num):
    try:
        return int(num) * int(num)
    except:
        return num * len(num)

# squared(5) would return 25
# squared("2") would return 4
# squared("tim") would return "timtimtim"
