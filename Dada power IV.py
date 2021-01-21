
>>> for i, c in enumerate('bonjour'):
	print(i, c)

0 b
1 o
2 n
3 j
4 o
5 u
6 r
>>> i = 0
>>> for c in 'bonjour':
	print(i, c)
	i += 1

0 b
1 o
2 n
3 j
4 o
5 u
6 r
>>> D = {'a': {1:3}, 'b': {2:5}}
SyntaxError: invalid character in identifier
>>> D = {'a': {1:3}, 'b': {2:5}}
>>> D['a'][1]
3
>>> D = {('a', 1):3, ('b', 2):5}
>>> D[('a', 1)]
3
>>> plus de pile ?
SyntaxError: invalid syntax
>>> skype, j'ai plus de battery dans mon tel :/
SyntaxError: EOL while scanning string literal
>>> 