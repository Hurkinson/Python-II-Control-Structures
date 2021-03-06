#Now let's make things a little more challenging.
#
#Last exercise, you wrote a function called word_count that
#counted the number of words in a string essentially by
#counting the spaces. However, if there were multiple spaces
#in a row, it would incorrectly add additional words. For
#example, it would have counted the string "Hi   David" as
#4 words instead of 2 because there are two additional
#spaces.
#
#Revise your word_count method so that if it encounters
#multiple consecutive spaces, it does *not* count an
#additional word. For example, these three strings should
#all be counted as having two words:
#
# "Hi David"
# "Hi   David"
# "Hi                 David"
#
#Other than ignoring consecutive spaces, the directions are
#the same: write a function called word_count that returns an
#integer representing the number of words in the string, or
#return "Not a string" if the input isn't a string. You may
#assume that if the input is a string, it starts with a
#letter word instead of a space.

#Write your function here!
def word_count(string):
    mL=[]
    m= ""
    try:
        
        if len(string) >=1 and string == str(string):
            #print("le string est valide")
            for c in string:  
                           
                try:
                    
                    if not c == " ":
                        m+= c
                        #print("{} est ajouté".format(c))
                        if string.index(c)+1 == len(string):
                            mL.append(m)
                            #print("{} est ajouté à la liste\n".format(m))
                            #print("fin de traitement du string")
                            #print(mL,"\n")
                        
                    else:
                        mL.append(m)
                        #print("{} est ajouté à la liste".format(m))
                        m= ""
                        #print("le mot est reset")
                        #print(mL[-1])
                        if mL[-1] == "": #dernière valeur de la liste
                            del mL[-1]
                            #print("espace supprimé\n")
                except:
                    pass
                
            return len(mL)
                        
    except:
        return "Not a string"
                        


#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#Word Count: 4
#Word Count: 2
#Word Count: Not a string
#Word Count: Not a string
#Word Count: Not a string

print("Word Count:", word_count("Four words are here!"))
print("Word Count:", word_count("Hi   David"))
print("Word Count:", word_count(5))
print("Word Count:", word_count(5.1))
print("Word Count:", word_count(True))


#---------------------------------------------------------------------------

#Like the last problem, there are multiple ways to do this,
#but many of them require things we haven't learned yet. So,
#let's first do this problem using what we've covered so
#far, and then in sample_answer_2.py you can find other
#ways to approach this.
#
#Our function definition hasn't changed:

def word_count(my_string):
    
    #And we still want to anticipate errors, so we wrap our
    #body in a try block:
    
    try:
        
        #Now, last time we went through the string and
        #counted the spaces. This time, however, we don't
        #want to count consecutive spaces. How can we do
        #that?
        #
        #The most straightforward way is to have a variable
        #that tells us if the previous character was a
        #space. If it was, we don't count a new space.
        #So, let's create that variable along with our
        #counter:
        
        word_count = 1
        previous_was_space = False
        
        #Then, we run the same loop we ran before:
        
        for letter in my_string:
            
            #But instead of counting if the current letter
            #is a space, we count if it's a space *and* the
            #previous letter wasn't a space. Effectively,
            #this means we're only counting the first space
            #when several appear in a row:
            
            if letter == " " and not previous_was_space:
                word_count += 1
            
            #Then, we have to update previous_was_space so
            #that it has the right value on the next
            #iteration of the loop:
            
            if letter == " ":
                previous_was_space = True
            else:
                previous_was_space = False
        
        #Then we can return the word count:
        return word_count
    
    #And as before, we return "Not a string" if we found a
    #TypeError:
    except TypeError:
        return "Not a string"
            
#------------------------------------------------------------------------

#The limitation of using a for-each loop in the previous
#solution is that we can only check one letter a time.
#That's why we had to manually track whether the previous
#letter was a space.
#
#What if we could actually peak at the "next" or "previous"
#letter? We can, using some syntax we'll cover in Chapter
#4.2:

def word_count(my_string):
    
    try:
        
        word_count = 1
        
        #Notice first that we're using a for loop instead of a
        #for-each loop. That's because we want to know the index
        #of each letter as we look at it. Notice also that we're
        #starting at the second letter -- we'll cover why in a
        #second.
        for i in range(1, len(my_string)):
            
            #Here's the unfamiliar syntax: the brackets let us
            #access the character at index i in the string. So,
            #if my_string is "Hi David!", my_string[0] will be
            #"H", my_string[1] will be "i", and so on.
            if my_string[i] == " ":
                
                #If we've reached here, we know the current
                #character is a space. Now we need to make sure
                #the letter before it wasn't a space. This line
                #checks the previous character, at index i - 1.
                #That's why we started the loop at 1, to avoid
                #checking the -1 character.
                
                if not my_string[i - 1] == " ":
                    
                    #If we've reached here, it means that the
                    #current character is a space, and the
                    #previous character was not a space. So, we
                    #can go ahead and count:
                    
                    word_count += 1
        
        #And now we're done, and can return our word count:
        return word_count
    
    except:
        return "Not a string"


#But maybe we're approaching this the wrong way in the first
#place. Instead of ignoring consecutive spaces while counting,
#why not just get rid of them?

def word_count(my_string):
    
    try:
        
        #This loop runs while the character sequence "  " is found
        #in ths string; in other words, as long as there are
        #consecutive spaces, this continues to run:
        
        while "  " in my_string:
            
            #This line will replace any instances of double spaces
            #with single spaces:
            
            my_string = my_string.replace("  ", " ")
        
        #That loop will continue to run as long as consecutive
        #spaces are found, which means that when it's done, there
        #should be no consecutive spaces. That means we can now
        #address the problem the way we did before:
        
        word_count = 1
        
        for letter in my_string:
            if letter == " ":
                word_count += 1
        return word_count
    
    except TypeError:
        return "Not a string"

#There are other ways to do this as well -- try out your own ideas
#and see what works!



