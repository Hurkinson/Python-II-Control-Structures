"""
Created on Wed Nov 18 19:10:16 2020

@author: Hurkinson

m= mot
c= character
L= Liste
D= Dictionnaire
ms=  my_string
mL= Liste de mots
"""
import itertools

#----------------------------------------------------------------------------

def mysplit(ms, sep=' '):   #(chaine de character cible, type de séparateur)
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

#----------------------------------------------------------------------------

def seeker(seek, mL):        #(élément à chercher, Liste cible)
    #print(mL)
    count= 0
    for m in mL:
        if m == seek:
            count += 1
    return count
     
#----------------------------------------------------------------------------

def get_counts(ms):
    mL = mysplit(ms)
    #print(mL)
    dico = {}
    for m in mL:
        if m in dico:
            dico[m] = dico[m] + 1
        else: 
            dico[m] = 1
            
    return dico

#----------------------------------------------------------------------------

def addict(item):        # itertools necessaire
    final= {}
    mot= "mot_"
    n = next(itertools.count(1))
    final[mot+str(n)] = item
    
    return final    