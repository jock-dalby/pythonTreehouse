for name in ['Jock', 'Nele', 'Alan']:
  print("Hello " + name)

my_list = ["Hello", "how", "are", "you"]
for word in my_list:
  print(word.upper())

for num in [1, 2, 3, 4]:
  if num % 2 == 0:
    print(num)

names = ['Jock', 'Nele', 'QUIT', 'Alan']
for name in names:
  if name == 'QUIT':
    break # break breaks the loop
  print(name)

names = ['Jock', 'Nele', 'QUIT', 'Alan']
for name in names:
  if name == 'QUIT':
    continue # continue skips a step
  print(name)
