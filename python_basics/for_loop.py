# Example 1
for name in ['Jock', 'Nele', 'Alan']:
  print("Hello " + name)

# Example 2
my_list = ["Hello", "how", "are", "you"]
for word in my_list:
  print(word.upper())

# Example 3
for num in [1, 2, 3, 4]:
  if num % 2 == 0:
    print(num)

# Example 4
names = ['Jock', 'Nele', 'QUIT', 'Alan']
for name in names:
  if name == 'QUIT':
    break # break breaks the loop
  print(name)

# Example 5
names = ['Jock', 'Nele', 'QUIT', 'Alan']
for name in names:
  if name == 'QUIT':
    continue # continue skips a step
  print(name)
