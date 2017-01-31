# python Basics

##python shell
When starting in Python and just want to play around with some ideas, you can use the Python shell. Sometimes this is called a REPL, R-E-P-L, which stands for
read–evaluate–print loop. To enter the shell, type 'python' in the console, to exit it, type 'exit()' or 'quit()' commands.

You can do math in the console e.g. 2 + 2 + enter = prints 4, run functions e.g. print('Hello, Treehouse').

Type 'help()' to access the help feature and put a keyword /phrase in the parentheses to search a specific term e.g. help(print), help(str) or help(str.center).

To run a python file from the shell, run 'python <filename>'

##Errors
A NameError happens whenever you try to use something that doesn't exist as far as python's concerned.

TypeError, which you get this for two reasons. Either you gave the wrong type of argument to a function, like if a function expected a number and you gave it a string or because you tried to do something that that particular type doesn't support. So you can't add a number and a string together.

The last common error is the SyntaxError.

##print()
```python
print('Hello, Treehouse')
```

##Integers

####round() & int()
```python
round(5.23) # Returns 5
round(5.73) # Returns 6
int(5.9) # Returns 5
int('5') # Returns 5
```

####float()
```python
float(5) # returns 5.0
float('8.2') # returns 8.2
```

##Strings
Strings are iterable (we can loop through them with for loops) and immutable (we're not allowed to change them in place).
```python
print('''He's right''') # returns 'He's Right'
print('=' * 5) # returns =====

status_message = 'Hey we have {} people using the site right now'
print(status_message.format(7))
# returns Hey we have 7 people using the site right now

status_message = 'Hey we have {} {} using the site right now'
print(status_message.format(5, 'dogs'))
# returns Hey we have 5 dogs people using the site right now
```

####split()
```python
'hello'.split() # returns ['hello']
'hello world'.split() # returns ['hello', 'world']
'red:green:blue'.split(':') # returns [red', 'green', 'blue]
```

##Booleans

####bool()
```python
True + True # Returns 2
bool(0) # False
bool([]) # False
bool([1, 2, 3, 4]) # True
bool('') # False
bool('Jock') # True
# Anything that empty is false. Anything which has content is true
```

##Variables
```python
my_name = 'Jock'
favourite_colour = 'purple'
favourite_number = 13

print(favourite_colour)
print(favourite_number - 5)

del favourite_number
print(favourite_number) # returns name 'favourite_number' is not defined
```

##Lists

####list()
```python
list('Hello') # returns ['H', 'e', 'l', 'l', 'o']
```

Lists in Python are a lot like arrays in other languages. Lists are iterable (we can loop through them with for loops) and mutable (we're allowed to change them in place).
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

del my_list[-1] # my_list is now [1, 2, 3, 4, 7, 8]
```

####insert(index no., item)
```python
my_list = ['a', 'b', 'c']

my_list.insert(1, 'd') # my_list is now ['a', 'd', 'b', 'c']

# Sort list and remove non-integers
messy_list = ['a', 2, 3, 1, False, [1, 2, 3]]
messy_list.insert(0, messy_list.pop(3))
del messy_list[1] # because 'a' is now at position 1
messy_list.remove(False)
messy_list.remove([1, 2, 3])
```

####remove()
```python
my_list = [1, 2, 3, 4, 1]
my_list.remove(1) # my_list is now [2, 3, 4]
```

####pop()
```python
names = ['jock', 'nele', 'paul', 'steve']
name_1 = names.pop() # name_1 now equals 'steve'
name_2 = names.pop(0) # name_2 now equals 'jock'


```

####join()
```python
flavours = ['chocolate', 'mint', 'strawberry']
', '.join(flavours) # returns 'chocolate', mint, strawberry'
'My favourite flavours are: {}'.format(', '.join(flavours)) # Returns 'My favourite flavours are chocolate, mint, strawberry'
```

####index()
```python
aplha = 'abcde'

alpha.index('a') # returns 0
'abcabc'.index('a') # returns 0
'bcabc'.index('a') # returns 2

alpha.index('cd') # returns 2
alpha.index('ce') # returns 'substring not found'

alpha[0] # returns 'a'
alpha[2] # returns 'c'

alpha[-2] # returns 'd'
alpha[-5] # returns 'a'

del alpha[0] # cannot delete from a string
alpha2 = list(alpha)
del alpha2[0] # alpha2 is now ['b', 'c', 'd', 'e']
```

####sort()
```python
my_list = [1, 4, 2, 5, 3]
new_list = my_list.sort() # new_list equals [1, 2, 3, 4, 5]
```

##Functions
```python
# Example 1
def answer_the_phone():
  greeting = 'Hi, this is Jock. Who is this?'
  print(greeting)

# Example 2
def lumberjack(name):
  if name.lower() == 'jock':
    print('Jock\'s a lumberjack and he\'s all sweet!')
  else:
    print('{} sleeps all night and {} works all day!'.format(name, name))

lumberjack('Jock')
lumberjack('Nele')

# Example 3
def lumberjack(name, pronoun):
    print('{}\'s a lumberjack and {} all sweet!').format(name, pronoun)

lumberjack('Sam', 'they\'re')

# Example 4
def average(num1, num2):
  return (num1 + num2) / 2

avg = average(2, 8)
print(avg)

# Example 5
def printer (count):
    print('Hi ' * count)
```

##Comparison operators
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

##User input()
```python
age = int(input('What\'s your age?')) #convert the string to a number
```

##Dictionaries

Dictionaries are made up of two pieces, a value that they want to hold onto and a key, the name we want to give to that value. Dictionaries like lists are mutable, so we can change them at will after they're created. But unlike lists dictionaries are unsorted, that means we can't use an index on them or even expect them to always look the same when we print them.

```python
# Example 1
course = {'title': 'Python Collections','teacher': {'first_name':'Kenneth', 'last_name': 'Smith'}}
course['title'] # returns Python Collections

# Loop through a dictionary and returna  list of tuples
for key, value in course.items():
  print("{} and {}".format(key, value))

# Example 2
player = dict([
  ['name', 'Jock'],
  ['remaining_lives', 3],
  ['levels', [1, 2, 3, 4]],
  ['items', {'oranges': 5}]
  ])

player['last_name'] = 'Dalby' # Add a single key:value pair to player dictionary

player.update({'job': 'Web Developer', 'editor': 'Atom'}) # Add multiple key:value pairs to player dictionary

player['editor'] = 'Webstorm' # Change editor value

# Delete a dictionary entry
del player['remaining_lives']

# Iterate through a dictionary
for entry in player:
  print(entry, player[entry])

# or separately
# keys
for key in player.keys():
  print(key)
#values
for value in player.values():
  print(value)
#both
for item in player.items():
  print(item)

# Example 3
player = {'weapons': {'sword': True, 'bow': False, 'stick': True}}
player['weapons']['sword']
```

####Packing, unpacking & kwargs
When we talk about packing, we're taking multiple inputs like multiple values and combining them into a single variable. Each value is still represented in the final variable so this isn't like adding two numbers together. When I'm talking about unpacking though, as you can probably guess, it's the opposite action unpacking takes the values in a variable and makes a bunch of new variables from it.

In Python, when you use double asterisks like below on a parameter in a function, Python will pack whatever keyword arguments come into the function into a dictionary. Because you're packing keyword arguments, you'll see this name, kwargs, for keyword arguments, quite often.

```python
# Example 1
def packer(**kwargs):
  print(kwargs)

packer(name='Jock', num=31, orange-pine-nuts=False) # returns {'name':'Jock', 'num': 31, orange-pine-nuts: False}

# Example 2
def packer(name=None, **kwargs):
  print(kwargs)

packer(name='Jock', num=31, orange-pine-nuts=False) # returns {'num': 31, orange-pine-nuts: False}

# Example 3
def unpacker(first_name=None, last_name=None):
  if first_name and last_name:
    print('Hi {} {}!'.format(first_name, last_name))
  else:
    print('Hi no name!')

unpacker(**{'last_name': 'Dalby', 'first_name': 'Jock'})
# Because of the two asterisks in front, python took each key from the dict and its value and sent them as keyword arguments to the function.
```

Write a function named string_factory that accepts a list of dictionaries as an argument. Return a new list of strings made by using ** for each dictionary in the list and the template string provided.
```python
template = "Hi, I\'m {name} and I love to eat {food}!"

def string_factory(dicts):
    strings = []
    for d in dicts: #<-- iterate over dict list
        strings.append(template.format(**d)) #<-- Append the new string to the strings list
    return strings
```
I need you to make a function named word_count. It should accept a single argument which will be a string. The function needs to return a dictionary. The keys in the dictionary will be each of the words in the string. The values will be how many times that particular word appears in the string.

```python
# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.

import collections

def word_count(word):
    new_list = word.lower().split()
    return collections.Counter(new_list)

```
The treehouse_teachers dictionary will look something like: {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections']}. Each key will be a Teacher and the value will be a list of courses.

```python
def num_teachers (treehouse_teachers):
    return len(treehouse_teachers)

#Create a new function named num_courses that will receive the treehouse_teachers dictionary as its only argument. The function should return the total number of courses for all of the teachers.
def num_courses(treehouse_teachers):
    counter = 0
    for key in treehouse_teachers.keys():
        counter += len(treehouse_teachers[key])
    return counter

#For this step, make another new function named courses that will, again, take the dictionary of teachers and courses and return a single list of all of the available courses in the dictionary. No teachers, just course names!

def courses(treehouse_teachers):
    all_courses = []
    for key in treehouse_teachers.keys():
        all_courses.extend(treehouse_teachers[key])
    return all_courses

# Create a function named most_courses that takes our good ol' teacher dictionary. most_courses should return the name of the teacher with the most courses. You might need to hold onto some sort of max count variable.

def most_courses(treehouse_teachers):
    max_count = 0
    for key in treehouse_teachers.keys():
        if len(treehouse_teachers[key]) > max_count:
            max_count = len(treehouse_teachers[key])
            top_teacher = key
    return top_teacher

# Create a function named stats and it'll take our teacher dictionary as its only argument. stats should return a list of lists where the first item in each inner list is the teacher's name and the second item is the number of courses that teacher has. For example, it might return: [["Kenneth Love", 5], ["Craig Dennis", 10]]

def stats(treehouse_teachers):
    stats_list = []
    for key in treehouse_teachers.keys():
        stats_list.append([key, len(treehouse_teachers[key])])
    return stats_list

```

##Tuples
Tuples are like lists in that each member has an index, they can be looped over and each member can be pretty much any other data type. Tuples, though, can't be changed in place as they're immutable. This also makes them a bit more memory efficient, which is always nice win. We can't add items, we can't pop items off and we can't even call del on our tuples but one fun little gotcha with tuples though, is that you can change the values inside of mutable tuple members. The only thing that I can't do is actually remove that list because that would be changing the tuple. I can do whatever I want to the inside of the list, though.

```python
my_tuple = (1, 2, 3) # conventional way of declaring a tuple
my_second_tuple = 1, 2, 3 # but parentheses are not essential. It is the comma that makes the Tuples
my_value = (5) # This would simply be 5

my_third_tuple = tuple([1, 2, 3]) # pass a list to the tuple function to convert my_third_tuple = (1, 2, 3)

my_third_tuple[0] = 5 # TypeError: 'tuple' object does not support item assignment

my_third_tuple[0] += 2 # TypeError: 'tuple' object does not support item assignment

tuple_with_a_list = (1, 'apple', [3, 4, 5])
tuple_with_a_list[2][1] = 6 # tuple_with_a_list now equals (1, 'apple', [6, 4, 5])
```

####Packing and unpacking tuples
```python
# Example 1
a = 5
b = 20
a, b = b, a # now a = 20 and b = 5

a = 5
b = 20
c = b, a # c is now equal to (5, 20)

# Example 2
def add(*nums):
  total = 0
  for num in nums:
    total += nums
  return total

add(5, 5) # 10
add(32) # 32

# or even better use below as then will know what value type to start total on

def add(base, *args):
  total = base
  for num in args:
    total += num
  return total

add(5, 20) # 25

# Example 3
def multiply(base, *args):
    total = base
    for arg in args:
        total *= arg
    return total

```

Enumerate takes an ordered iterable like a list or a string or a tuple. Then it walks through that iterable and for each item in it gives us back a tuple of the current index and the value at that index.
```python
# Example 1
list(enumerate("abc")) # [(0, 'a'), (1, 'b'), (2, 'c')]

# Example 2
my_list = [5, 2, 4, 1, 3]
for index, value in enumerate(my_list):
  print("{}: {}".format(index, value))
# returns
# 0: 5
# 1: 2
# 2: 4
# 3: 1
# 4: 3

# or

for group in enumerate(my_list):
  print("{}: {}".format(*group)
  )

# Example 3
for index, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
    print('{}: {}'.format(index+1, letter)
    )
```

####Challenges

##Challenge 1
Create a function named stringcases that takes a single string but returns a tuple of different string formats. The formats should be:
- All uppercase
- All lowercase
- Titlecased (first letter is capitalized)
- Reversed

```python
def stringcases (my_str):
    return my_str.upper(), my_str.lower(), my_str.title(), my_str[-1::-1]
```

##Challenge 2
Create a function named combo that takes two ordered iterables. These could be tuples, lists, strings, whatever. Your function should return a list of tuples. Each tuple should hold the first item in each iterable, then the second set, then the third, and so on. Assume the iterables will be the same length.

```python
def combo(iter1, iter2):
  tup_list = []
  count = 0

  for thing in iter2:
    tup = tuple((iter1[count], iter2[count]))
    tup_list.append(tup)
    count +=1

  return tup_list
```

For a more advanced solution, you can use the built-in zip function (covered later) that "zips" two iterables together by returning one item from each iterable as a tuple. Wrapping this in a list() provides the complete solution:

```python
def combo(iter1, iter2):
  return list(zip(iter1, iter2))
```

##Sets

A set is a collection of unique items that belong together for some reason. Each thing can only be in a given set once and Python sets are iterable collections like list and tuples, but each item is unique and the set doesn't have any indexes. It used to be the case that you could only create sets by using the set function, but in modern Python versions you can use the curly braces to directly create a set so long as your set has something in it.

```python
set([1, 3, 5]) # creates set => {1, 3, 5}
{1, 3, 5} # creates set => {1, 3, 5}
```
If you try to create a blank set though, you'll get a dictionary. In that case you have to use, the set function so that typeset gives you a set.

```python
type({}) # returns 'dict'
type(set()) # returns 'set'
```

Now the order that you put things into sets doesn't matter as sets don't have a defined order or any indexes and we can get them back in a different order; Python sorts the sets in a way that makes sense to Python.

####Adding to a set

```python
low_primes = {1, 3, 5, 7, 11, 13}
low_primes.add(17) # low_primes = {1, 3, 5, 7, 11, 13, 17}
low_primes.update({19, 23}, {2, 29}) # {1, 2, 3, ... 19, 23, 29}
```

####Removing from a set

```python
low_primes = {1, 3, 5, 7, 11, 13}
low_primes.add(4) # low_primes = {1, 3, 4, 5, 7, 11, 13}
low_primes.remove(4) # low_primes = {1, 3, 5, 7, 11, 13}

one_prime = low_primes.pop()
```

####Set maths

Sets have several different operations that they can do.

#####Union => All of the items from all of the sets
```python
set1 = set(range(10))
set2 = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23}

set1.union(set2) # => {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 17, 19, 23}

# or can get the same result using the | character

set1 | set2 # => {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 17, 19, 23}
```

##### Difference => All of the items in the first set that are not in the other sets
```python
set1 = set(range(10))
set2 = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23}

set1.differnece(set2) # => {0, 8, 4, 6, 9}
set2.difference(set1) # => {19, 17, 11, 13, 23}

# or can get the same result using the - character

set1 - set2 # => {0, 8, 4, 6, 9}
set2 - set1 # => {19, 17, 11, 13, 23}
```

#####Intersection => All of the common items between all of the sets
```python
set1 = set(range(10))
set2 = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23}

set1.intersection(set2) # => {1, 2, 3, 5, 7}

# or can get the same result using the & character

set1 & set2 # => {1, 2, 3, 5, 7}
```

######Symmetric difference => all of the items that are not shared by the two sets
```python
set1 = set(range(10))
set2 = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23}

set1.symmetric_difference(set2) # => {0, 4, 6, 8, 9, 11, 13, 17, 19, 23}

# or can get the same result using the ^ character

set1 ^ set2 # => {0, 4, 6, 8, 9, 11, 13, 17, 19, 23}
```

#####Example Challenges

Write a function named covers that accepts a single parameter, a set of topics. Have the function return a list of courses from COURSES where the supplied set and the course's value (also a set) overlap.

```python

```
