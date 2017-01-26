# python Basics

####python shell
When starting in Python and just want to play around with some ideas, you can use the Python shell. Sometimes this is called a REPL, R-E-P-L, which stands for
read–evaluate–print loop. To enter the shell, type 'python' in the console, to exit it, type 'exit()' or 'quit()' commands.

You can do math in the console e.g. 2 + 2 + enter = prints 4, run functions e.g. print("Hello, Treehouse").

Type 'help()' to access the help feature and put a keyword /phrase in the parentheses to search a specific term e.g. help(print), help(str) or help(str.center).

To run a python file from the shell, run 'python <filename>'

####Errors
A NameError happens whenever you try to use something that doesn't exist as far as python's concerned.

TypeError, which you get this for two reasons. Either you gave the wrong type of argument to a function, like if a function expected a number and you gave it a string or because you tried to do something that that particular type doesn't support. So you can't add a number and a string together.

The last common error is the SyntaxError.

####print()
```python
print("Hello, Treehouse")
```

####variables
```python
my_name = "Jock"
favourite_colour = "purple"
favourite_number = 13

print(favourite_colour)
print(favourite_number - 5)

del favourite_number
print(favourite_number) # returns name 'favourite_number' is not defined
```

####strings
```python
print("""He's right""") # returns "He's Right"
print('=' * 5) # returns =====

status_message = "Hey we have {} people using the site right now"
print(status_message.format(7))
# returns Hey we have 7 people using the site right now

status_message = "Hey we have {} {} using the site right now"
print(status_message.format(5, 'dogs'))
# returns Hey we have 5 dogs people using the site right now
```

####functions
```python
# Example 1
def answer_the_phone():
  greeting = "Hi, this is Jock. Who is this?"
  print(greeting)

# Example 2
def lumberjack(name):
  if name.lower() == "jock":
    print("Jock's a lumberjack and he's all sweet!")
  else:
    print("{} sleeps all night and {} works all day!".format(name, name))

lumberjack("Jock")
lumberjack("Nele")

# Example 3
def lumberjack(name, pronoun):
    print("{}'s a lumberjack and {} all sweet!").format(name, pronoun)

lumberjack("Sam", "they're")

# Example 4
def average(num1, num2):
  return (num1 + num2) / 2

avg = average(2, 8)
print(avg)

# Example 5
def printer (count):
    print("Hi " * count)
```

####round() & int()
```python
round(5.23) # Returns 5
round(5.73) # Returns 6
int(5.9) # Returns 5
int("5") # Returns 5
```

####float()
```python
float(5) # returns 5.0
float("8.2") # returns 8.2
```

####list()
```python
list('Hello') # returns ['H', 'e', 'l', 'l', 'o']
```

####lists
Lists in Python are a lot like arrays in other languages.
```python
my_list = [1, 2, 3]
print(my_list + [4, 5]) # prints [1, 2, 3, 4, 5])
my_list += [4, 5] # my_list is now [1, 2, 3, 4, 5]
mylist *= 2 # my_list is now [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

my_list = [1, 2, 3]
my_list.append(4) # my_list is now [1, 2, 3, 4]
my_list.append([5, 6]) # my_list is now [1, 2, 3, 4, [5, 6]]
my_list.extend([7, 8, 9]) # my_list is now [1, 2, 3, 4, [5, 6], 7, 8, 9]

my_list.remove([5, 6]) # my_list is now [1, 2, 3, 4, 7, 8, 9]
```

####bool()
```python
True + True # Returns 2
bool(0) # False
bool([]) # False
bool([1, 2, 3, 4]) # True
bool("") # False
bool("Jock") # True
# Anything that empty is false. Anything which has content is true
```

####Comparison operators
```python
5 == 5 # True
5 == 7 # False
5 != 7 # True
5 < 7 # True
5 > 7 # False
5 <= 7 # True

5 is 5 # True
c = []
d = []
c == d # True
c is d # False
# 'is' tests to see if the two values are in the same place in memory (essentially ===)
```
