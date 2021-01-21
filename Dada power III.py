mystery_string = "my cat your cat"

import collections


ms = mystery_string
ms_L = ms.split()
msDc = collections.Counter(ms_L)

print(ms_L, msDc)

#------------------------------------------------------

def mysplit(ms):
    
    mL = []
    m  = ''
    for c in ms:
        if c == " ":
            mL.append(m)
            m = ''
        else:
            m += c
    
    mL.append(m)
    print(mL)


mysplit(mystery_string)

mysplit('salut les gars')



print('salut les gars\nça va ?'.split(' '))
print('salut les gars\nça va ?'.split('\n'))
print('salut les gars\nça va ?'.split())


#------------------------------------------------------------

import sys

sys.path.append("C:\\Users\\Hurkinson\\.spyder-py3\\plugins")
sys.path.append(r"C:\Users\Hurkinson\.spyder-py3\plugins")
"""
Created on Wed Nov 18 19:12:18 2020

@author: Hurkinson
"""

import toolbox

print(sys.path)

print(toolbox.mysplit("hello toto"))

#---------------------------------------------------------------------

mot_a_chercher='cat'

def mysplit(ms, sep=' '):
    #print(ms)
    mL = []
    m  = ''
    for c in ms:
        if c == sep:
            mL.append(m)
            m = ''
        else:
            m += c
    
    mL.append(m)
    #print(mL)
    return mL

def get_counts(mL):
    #print(mL)
    dico = {}
    for m in mL:
        if m in dico:
            dico[m] = dico[m] + 1
        else: 
            dico[m] = 1
            
    return dico       


ms_L = mysplit(mystery_string)

print(get_counts(ms_L))
#--------------------------------------------------------


import itertools
count = itertools.count(1)

for i in range(1,len(mystery_string)+1):
    print(mystery_string[0:next(count)])
        
print()


#------------------------------------------------
import toolbox

fn = r"C:\Users\Hurkinson\.spyder-py3\Pjointes\plantes.txt"
with open(fn, 'r', encoding='utf8') as f:
    s = f.read()

lineL = toolbox.mysplit(s,"\n")

vLL = [toolbox.mysplit(line,"\t")  for line in lineL]
print(vLL)

for french, latin, uniprot in vLL:
    print('la plante', french, 'a pour numero uniprot', uniprot)