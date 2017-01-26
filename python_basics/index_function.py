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
