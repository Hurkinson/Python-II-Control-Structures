mystery_string = "catcatcatcat"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Add some code below that will count and print how many
#times the character sequence "cat" appears in mystery_string.
#For example, for the string above, it would print 2.
#
#This one is tricky! Think carefully about for-each loops,
#conditionals, and booleans. How can you track what character
#you're currently looking for? We expect you'll use a loop
#and a single big conditional, but there are other approaches
#as well. Try to stick with the topics we've covered so far.


#Add your code here!
string = mystery_string
target="cat"

mL=[]
m= ""

if target in string: 

    for globalcount in range(len(string)):                             
        for mcount in range(len(target)):
            
            if string[globalcount] == target[mcount]:
                m += string[globalcount]
                if m == target[0:len(m)]:                    
                    if len(m) == len(target):
                        if m == target:
                            mL.append(m)
                            m= ""
                            
                else:
                    m= m[:-1]
 
print(len(mL))

#----------------------------------------------------------------  
    
sequence = "cat"
start = 0
end = len(sequence)
count = 0

while end <= len(mystery_string):
    if sequence == mystery_string[start:end]:
        count += 1
    start += 1
    end += 1

print(count)

#----------------------------------------------------------------

mystery_string = "my cat your cat"

#Later on, we'll cover lots of other ways to do this, using
#more sophisticated approaches to using substrings and other
#concepts. We can still do this using just what we know now,
#though!
#
#First, we know we need a counter since the problem says to
#count something:

count = 0

#Next, we need to keep track of what letter we're currently
#searching for. The first letter in "cat" is "c", so by
#default, we'll set this to "c":
current_search_letter = "c"

#Then, we loop over all the letters in the string:
for letter in mystery_string:
    
    #For each letter, we want to see if it's the letter
    #we're looking for.
    #
    #If it's a 'c' and we're looking for 'c', great! Now
    #we're looking for 'a':
    if letter == "c":
        current_search_letter = "a"
        
    #If it's an 'a' and we're looking for 'a', great! Now
    #we're looking for 't':
    elif letter == "a" and current_search_letter == "a":
        current_search_letter = "t"
        
    #If it's a 't' and we're looking for 't', then we've
    #found the word 'cat'! So, we add one to the counter,
    #and start over looking for 'c' again:
    elif letter == "t" and current_search_letter == "t":
        count += 1
        current_search_letter = "c"
     
    #Here's the trick: if we find any letter other than the
    #one we were looking for, then we need to start over!
    #If we've found "ca" but the next letter is "b", then
    #it doesn't matter if the one after it is "t": "cabt"
    #isn't the same as "cat":
    else:
        current_search_letter = "c"
print(count)


#----------------------------------------------------------------
#test:
    
string = "cyugairdcat"
target="cat"

def addict(item,value):       
    Dic= {}
    Dic[str(item)] = value
    
    return Dic
globalcount= 0
mL=[]
m= ""
ws_limite= addict(string[globalcount],0)     #ws pour wrong statment
ws= 0

if target in string: 
    print("\n\nle mot", target,"est dans", string,".\nResultat de la recherche:\n\n")

    for globalcount in range(len(string)):                       
        print("itération",globalcount, ",lettre:", string[globalcount], sep="\t")
        for mcount in range(len(target)):
            if string[globalcount] == target[mcount]:
                print("lettre str:", string[globalcount], "lettre cible:", target[mcount] )
                m += string[globalcount]
                print("lettre", string[globalcount], "présente dans", target,", ajout de", string[globalcount], "dans la liste: ok")
                print("liste:",m,"\n")
                if m == target[0:len(m)]:                    
                    if len(m) == len(target):
                        if m == target:
                            mL.append(m)
                            m= ""
                            
                else:
                    print("SUPPRESSION de :", string[globalcount],"\nLettre incorrecte ou mal placée","\n")
                    m= m[:-1]
            else:
                
                for a in ws_limite.keys:
                    ws +=1
                    if ws == ws_limite:
                        print("Lettre", string[globalcount], "non présente dans", target,"\n")
                    
else:
    print("\n\nle mot", target, "n'est pas présent dans", string, ".\n\n")                    

m= ""
print("--------------------------------------------------------------")
print("Fin de la recherche:\n")
print("il y a", len(mL), target, "dans" , string)