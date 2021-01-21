a = (2, 'oui', 5, 7)
for x in a:
	print(x)

2
oui
5
7
a=((2, 'oui'), (3, 4), (2, 'toto'))
for x in a :
	print(x)

(2, 'oui')
(3, 4)
(2, 'toto')
a = 2
b = 'oui'
a, b = (2, 'oui')
b
'oui'

for a, b in ((2, 'oui'), (3, 4), (2, 'toto')) :
	print('a=', a, 'b=', b)

a= 2 b= oui
a= 3 b= 4
a= 2 b= toto

# ----------------------- 
quarters_value = 25
quarters = amount // quarters_value
amount -= quarters*quarters_value
print('quarters=', quarters, 'amount=', amount)

# ----------------------- 
countdown = amount

quarters_value = 25
quarters = 0
while countdown >= quarters_value :
    quarters += 1
    countdown -= quarters_value
print(quarters, 'quarters', 'reste', countdown)

# ----------------------- 
quarters_value = 25
quarters = 0

def quarters_amm():
    return quarters*quarters_value

while quarters_amm() <= countdown :
    quarters += 1

    
# ----------------------- 
quarters_value = 25
quarters = 0

quarters_amm = quarters*quarters_value
while quarters_amm <= countdown :
    quarters += 1
    quarters_amm = quarters*quarters_value
quarters -= 1
print(quarters_nb, 'quarters', 'reste', countdown)

# ----------------------- 
quarters = amount // quarters_value
amount -= quarters*quarters_value
print('quarters=', quarter, 'amount=', amount)

countdown  = amount
for value, name in ((25, 'quarters'), (10, 'dimes'), (5, 'nickels'), (1, 'pennies')):
    nombre = countdown // value
    countdown -= nombre*value
    print(nombre, name, 'reste', countdown)

# ----------------------- 
    
import random

random = float(random.choice(range(85,101))/100)

# ----------------------- 
