>>>a, b = 3, 4
>>>a
3
>>>b
4

>>> print("Il est temps de faire un point sur l'heure")
Il est temps de faire un point sur l'heure


>>> import datetime
>>> print(datetime.datetime.now())
2020-11-04 19:35:28.954450

>>> def point_heure():
	print("Il est temps de faire un point sur l'heure")
	print(datetime.datetime.now())
	print("voilà tu connais l'heure")


>>> point_heure()
Il est temps de faire un point sur l'heure
2020-11-04 19:37:18.228888
voilà tu connais l'heure



>>> point_heure = """il est temps de faire un point sur l'heure\n""" + str(datetime.datetime.now()) + "voilà tu connais l'heure"""
>>> print(point_heure)
il est temps de faire un point sur l'heure
2020-11-04 19:38:36.637229voilà tu connais l'heure

>>> point_heure = """il est temps de faire un point sur l'heure\n""" + str(datetime.datetime.now()) + "voilà tu connais l'heure"""

>>> point_heure
"il est temps de faire un point sur l'heure\n2020-11-04 19:38:52.505749voilà tu connais l'heure"

>>> point_heure
"il est temps de faire un point sur l'heure\n2020-11-04 19:38:52.505749voilà tu connais l'heure"

>>> def point_heure():
	print("Il est temps de faire un point sur l'heure")
	print(datetime.datetime.now())
	print("voilà tu connais l'heure")

	
>>> a = point_heure()
Il est temps de faire un point sur l'heure
2020-11-04 19:40:13.972908
voilà tu connais l'heure

>>> def moyenne(a, b):
	return (a + b)/2

>>> moyenne(2,5)
3.5
>>> moyenne(4,8)
6.0
>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

>>> d = { 'bonjour' : 7, 'oui' : 3, 'non': 3}
>>> d
{'bonjour': 7, 'oui': 3, 'non': 3}

>>> d['oui']
3
>>> d['bonjour']
7
>>> d['non']
3
>>> a=34
>>> toto = 23
>>> locals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'datetime': <module 'datetime' from '/usr/lib/python3.6/datetime.py'>, 'point_heure': <function point_heure at 0x7fa43464f6a8>, 'a': 34, 'moyenne': <function moyenne at 0x7fa43464f9d8>, 'math': <module 'math' (built-in)>, 'd': {'bonjour': 7, 'oui': 3, 'non': 3}, 'toto': 23}

>>> locals()['toto']
23
>>> toto
23
>>> print(4, 5, 7)
4 5 7
>>> print(4, 5, 7, sep='\')
4\5\7
>>> print(4, 5, 7, sep='\n')
4
5
7

>>> texte = 'bonjour monsieur aunirestaunri'
>>> liste = ['13', 14, 'bonjour']
>>> tuple = (4, 47, 'coucou')
>>> for a in texte:
	print(a)

b
o
n
j
o
u
r
 
m
o
n
s
i
e
u
r
 
a
u
n
i
r
e
s
t
a
u
n
r
i
>>> for a in liste:
	print(a)

13
14
bonjour
>>> for a in tuple:
	print(a)

4
47
coucou
>>> for z in tuple:
	print(z)

4
47
coucou
>>> z
'coucou'
>>> locals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'datetime': <module 'datetime' from '/usr/lib/python3.6/datetime.py'>, 'point_heure': <function point_heure at 0x7fa43464f6a8>, 'a': 'coucou', 'moyenne': <function moyenne at 0x7fa43464f9d8>, 'math': <module 'math' (built-in)>, 'd': {'bonjour': 7, 'oui': 3, 'non': 3}, 'toto': 23, 'texte': 'bonjour monsieur aunirestaunri', 'liste': ['13', 14, 'bonjour'], 'tuple': (4, 47, 'coucou'), 'z': 'coucou'}
>>> t = (34, 45, 7, 5, 8)
>>> def moyenne(xL):
	somme = 0
	for x in xL:
		somme += x
	return somme/len(xL)

>>> moyenne(t)
19.8
>>> bourse = 80
>>> while bourse > 7:
	print("achat d'un objet à 7 euros")
	bourse -= 7

achat d'un objet à 7 euros
achat d'un objet à 7 euros
achat d'un objet à 7 euros
achat d'un objet à 7 euros
achat d'un objet à 7 euros
achat d'un objet à 7 euros
achat d'un objet à 7 euros
achat d'un objet à 7 euros
achat d'un objet à 7 euros
achat d'un objet à 7 euros
achat d'un objet à 7 euros


>>> personneL = (('gérard', 67), ('marcel', 89), ('henriette', 82))
>>> personneL
(('gérard', 67), ('marcel', 89), ('henriette', 82))
>>> for nom_age in personneL:
	print(nom_age)

('gérard', 67)
('marcel', 89)
('henriette', 82)
>>> for nom_age in personneL:
	print(nom_age[0] + 'est agé de ' + str(nom_age[1]) + ' ans')

gérardest agé de 67 ans
marcelest agé de 89 ans
henrietteest agé de 82 ans
>>> nom_age[0]
'henriette'
>>> personneL[0]
('gérard', 67)
>>> nom, age = personneL[0]
>>> nom
'gérard'
>>> age
67


>>> nom_age = personneL[0]
>>> nom_age = personneL[1]

>>> for nom, age in personneL:
	print(nom + 'est agé de ' + str(age) + ' ans')
	
gérardest agé de 67 ans
marcelest agé de 89 ans
henrietteest agé de 82 ans

#----------------------------------------------------------------------------

>>> ab, c = (5, 6), 7
>>> ab
(5, 6)

>>> (a, b), c = (5, 6), 7
>>> a
5
>>> b
6
>>> c
7

#----------------------------------------------------------------------------

>>> personneD = dict(personneL)
>>> personneD
{'gérard': 67, 'marcel': 89, 'henriette': 82}

>>> personneD.keys()
dict_keys(['gérard', 'marcel', 'henriette'])
>>> personneD.values()
dict_values([67, 89, 82])
>>> personneD.items()
dict_items([('gérard', 67), ('marcel', 89), ('henriette', 82)])
>>> for nom, age in personneD.items():
	print(nom + 'est agé de ' + str(age) + ' ans')

gérardest agé de 67 ans
marcelest agé de 89 ans
henrietteest agé de 82 ans
>>> for et in personneD:
	print(et)

gérard
marcel
henriette

>>> 'jean' in personneD
False

>>> 'gérard' in personneD
True

>>> 89 in personneD
False

>>> type(personneD)
<class 'dict'>

>>> personneD.keys()
dict_keys(['gérard', 'marcel', 'henriette'])


>>> personneD.update((('annette',88), ('georgette', 103)))
>>> personneD
{'gérard': 67, 'marcel': 89, 'henriette': 82, 'annette': 88, 'georgette': 103}
>>> dir(personneD)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

>>> personneD.pop('annette')
88
>>> personneD
{'gérard': 67, 'marcel': 89, 'henriette': 82, 'georgette': 103}

>>> personneD['gérard']
67
>>> personneD
{'gérard': 67, 'marcel': 89, 'henriette': 82, 'georgette': 103}

>>> a, b = personneD.popitem()
>>> a
'georgette'
>>> b
103

#----------------------------------------------------------------------------

>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> math.tan(3)
-0.1425465430742778
>>> import datetime
>>> dir(datetime)
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
>>> maintenant = datetime.datetime.now()
>>> maintenant.strftime('%W %Y %d')
'44 2020 04'
>>> maintenant.strftime('%W %Y %m %d')
'44 2020 11 04'
>>> maintenant.strftime('%W %Y %p %m %d')
'44 2020 PM 11 04'
>>> maintenant.strftime('%W %Y %p %m %d %H:%M:%S')
'44 2020 PM 11 04 20:34:16'
>>> maintenant.isoformat()
'2020-11-04T20:34:16.959636'

>>> apres = datetime.datetime.now()
>>> instantL = [maintenant, apres]
>>> instantL
[datetime.datetime(2020, 11, 4, 20, 34, 16, 959636), datetime.datetime(2020, 11, 4, 20, 37, 25, 229343)]
>>> instantstrL = [instant.isoformat() for instant in instantL]

>>> instantstrL
['2020-11-04T20:34:16.959636', '2020-11-04T20:37:25.229343']


#----------------------------------------------------------------------------

>>> xL = [2, 3, 4, 5]
>>> carreL = [x*x for x in xL]
>>> carreL
[4, 9, 16, 25]
>>> mutation_de_liste = [expression for element in liste]

#----------------------------------------------------------------------------

>>> instantstrL
['2020-11-04T20:34:16.959636', '2020-11-04T20:37:25.229343']
>>> dir(instantstrL)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

>>> instantstrL.sort()
>>> instantstrL
['2020-11-04T20:34:16.959636', '2020-11-04T20:37:25.229343']

>>> instantstrL.sort(reverse=True)
>>> instantstrL
['2020-11-04T20:37:25.229343', '2020-11-04T20:34:16.959636']

>>> instantL.sort()

#----------------------------------------------------------------------------

>>> a = 'bonjour'
>>> a = list(a)
>>> a
['b', 'o', 'n', 'j', 'o', 'u', 'r']

>>> a.sort()
>>> a
['b', 'j', 'n', 'o', 'o', 'r', 'u']

>>> a[1]
'j'

>>> print(a)
['b', 'j', 'n', 'o', 'o', 'r', 'u']

>>> a.sort()
>>> sorted('bonjour')
['b', 'j', 'n', 'o', 'o', 'r', 'u']

#----------------------------------------------------------------------------

>>> set('bonjour')
{'r', 'j', 'b', 'o', 'u', 'n'}

>>> sorted(set('bonjour'))
['b', 'j', 'n', 'o', 'r', 'u']

>>> set('bonjour') & set('au revoir')
{'r', 'o', 'u'}

>>> set('bonjour') - set('au revoir')
{'j', 'b', 'n'}

>>> set('bonjour') + set('au revoir')

Traceback (most recent call last):
  File "<pyshell#217>", line 1, in <module>
    set('bonjour') + set('au revoir')
TypeError: unsupported operand type(s) for +: 'set' and 'set'

>>> set('bonjour') | set('au revoir')
{'r', 'j', 'v', 'b', 'a', ' ', 'o', 'u', 'e', 'n', 'i'}

>>> set('bonjour') and set('au revoir')
{'r', 'v', ' ', 'o', 'i', 'u', 'e', 'a'}

#----------------------------------------------------------------------------


>>> 0 or False or [] or 0.0 or 'a' or 13 or 'coucou'
'a'
>>> 1 and 3 and 'a' and [] and 0
[]

>>> a=3
>>> inverse = a and 1/a
>>> inverse
0.3333333333333333

>>> a=0
>>> inverse = a and 1/a
>>> inverse
0

>>> a=None
>>> inverse = a and 1/a
>>> inverse
>>> inverse is None
True
>>> 
