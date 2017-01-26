'hello'.split() # returns ['hello']
'hello world'.split() # returns ['hello', 'world']
'red:green:blue'.split(':') # returns [red', 'green', 'blue]

flavours = ['chocolate', 'mint', 'strawberry']
', '.join(flavours) # returns 'chocolate', mint, strawberry'
"My favourite flavours are: {}".format(', '.join(flavours)) # Returns 'My favourite flavours are chocolate, mint, strawberry'
