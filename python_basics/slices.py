# A slice put as simply as possible, is a new list or string that's made from part of another list or string. If you make a slice from a list, you'll get a list. If you make a slice from a string, you'll get a string.

#Examples 1
my_list = [1, 2, 3, 4, 5, 6, 7]
new_list = my_list[1:5] # new_list now equals [2, 3, 4, 5]

new_list_2 = my_list[:2] # goes from start to index 2
new_list_3 = my_list[5:] # goes from index 5 to end

new_list_4 = my_list[5:100] # if not 100 indexes long will just go from 5 to end

new_list_5 = my_list[:] # makes a copy of the list from beginning to end

#Example 2
favorite_things = ['raindrops on roses', 'whiskers on kittens', 'bright copper kettles',
                   'warm woolen mittens', 'bright paper packages tied up with string',
                   'cream colored ponies', 'crisp apple strudels']

slice1 = favorite_things [1:4] #'whiskers on kittens', 'bright copper kettles', 'warm woolen mittens'
slice2 = favorite_things [-2:] #'cream colored ponies', 'crisp apple strudels'

sorted_things = favorite_things[:]
sorted_things.sort()

#Example 3
numbers = list(range(20)) # [0, 1, 2 ... 17, 18, 19]
numbers[::2] # first colon is for start and stop indexes, and then another colon followed by an integer which is the 'step' => returns [0, 2, 4 ... 14, 16, 18]

numbers[::-1] # returns [19, 18, 17 ... 2, 1, 0]
numbers[2:9:2] # returns [2, 4, 6, 8]
numbers[-2:-5:-1] # returns [18, 17, 16]

# Example 4
def first_4(iterable):
    return iterable[:4]

#Make a new function named first_and_last_4. It'll accept a single iterable but, this time, it'll return the first four and last four items as a single value.
def first_and_last_4(iterable):
    first_4 = iterable[:4]
    last_4 = iterable[-4:]
    first_4.extend(last_4)
    return first_4

# Create a new function named odds that returns every item with an odd index in a provided iterable. For example, it would return the items at index 1, 3, and so on.

def odds (iterable):
    return iterable[1::2]

#Make a function named reverse_evens that accepts a single iterable as an argument. Return every item in the iterable with an even index...in reverse. For example, with [1, 2, 3, 4, 5] as the input, the function would return [5, 3, 1].

def reverse_evens (iterable):
    if len(iterable) % 2 == 0:
        return iterable[-2::-2]
    else:
        return iterable[-1::-2]


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del my_list[5:8] # list now equals [0, 1, 2, 3, 4, 8, 9, 10]
my_list[5:8] = [5, 6, 7] # list now equals [0, 1, 2, 3, 4, 5, 6, 7]
my_list[-4:] = ''.join('etc.') # list now equals [0, 1, 2, 3, 'etc.']

#This one will be named sillycase and it'll take a single string as an argument. sillycase should return the same string but the first half should be lowercased and the second half should be uppercased. For example, with the string "Treehouse", sillycase would return "treeHOUSE".

def sillycase (str):
    halfway = int(len(str) / 2)
    first_half = str[:halfway].lower()
    last_half = str[halfway:].upper()
    return first_half + last_half
