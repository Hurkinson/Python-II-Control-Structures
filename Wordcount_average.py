#This will be the largest, most authentic program you've
#written so far. It will require everything you've learned
#and should take some time to test and debug. Be patient,
#you can do it!
#
#Write a function called average_word_length that takes as
#input a string called my_string, and returns as output the
#average length of the words in the string.
#
#In writing this function, note the following:
#
# - You should account for consecutive spaces. A string like
#   "Hi   Lucy" is two words with an average length of 3.0
#   characters.
# - You should not assume the string starts with a letter.
#   A string like "  David" has one word with an average
#   length of 5.0 characters.
# - You should not count punctuation marks toward the
#   length of a word. A string like "Hi, Lucy" has two
#   words with an average length of 3.0 characters: the ,
#   after "Hi" does not count as a character in the word.
#   The only punctuation marks you need to handle are
#   these: . , ! ?
# - You may assume the only characters in the string are
#   letters, the punctuation marks listed above, and spaces.
# - If my_string is not a string, you should instead return
#   the string, "Not a string".
# - If there are no words in my_string, you should instead
#   return the string, "No words". This could happen for
#   strings like "" (an empty string) and ".,!?" (a string
#   of only punctuation marks). You may assume that any
#   of these punctuation marks will always be followed by
#   at least one space.
#
#Here are a few hints that might help you:
#
# - You can peak at the first character in my_string with
#   my_string[0]. If my_string is "Hi, Lucy", then the value
#   of my_string[0] is "H". You don't have to do this, but
#   you can if you want.
# - There are lots of ways you can do this. If you're
#   stuck, try taking a step back and thinking about the
#   problem from a fresh perspective.
# - If you're still stuck, try counting words and letters
#   separately, and worrying about average length only
#   after both have been counted.
# - The word count should equal the number of letters that
#   come immediately after a space or the start of the
#   string. The character count should simply equal the
#   number of characters besides spaces and punctuation
#   marks. The average word length should be character
#   count divided by word count.


#Write your function here!
def average_word_length(string):

    mL=[] #Words in str
    lC= 0 #letter Count
    m= "" #current word
    tracker = 1
    try:
        
        if type(string) == type("toto"):
            print("le string est valide")
            try:
                
                if len(string) >=1:
                    print("le string est plein")
                    for c in string:  
                                   
                        try:
                            
                            if not c == " ":
                                if c in ". , ! ?":
                                    print("{} catched".format(c))
                                    if tracker == len(string):
                                        print("fin de mot")
                                        if len(mL) == 0:
                                            return "No words"
                                        mL.append(m)
                                        print(mL,"\n")
                                    
                                
                                else:
                                    m+= c
                                    lC+=1
                                    print(lC)
                                    print("{} est ajouté".format(c))
                                    print("index de c en cour = ", tracker)
                                    print("taille du string = ",len(string))
                                    if tracker == len(string):
                                        mL.append(m)
                                        print("{} est ajouté à la liste\n".format(m))
                                        print("fin de traitement du string")
                                        print(mL,"\n")
                                
                            else:
                                mL.append(m)
                                print("{} est ajouté à la liste".format(m))
                                m= ""
                                print("le mot est reset")
                                print(mL[-1])
                                if mL[-1] == "": #dernière valeur de la liste
                                    del mL[-1]
                                    print("espace supprimé\n")
                                    
                        except Exception as error:
                            return error
                        finally:
                            tracker +=1
                            
                    return lC / len(mL)
                
                
                
                else:
                    return "No words"
                
            except Exception as error:
                return error 
        else:
            return "Not a string"
        
    except Exception as error:
        return error


#When your function works, the following code should
#output:
#2.0
#3.0
#4.0
#Not a string
#No words


#----------------------------------------------------------------------


#As before, there are lots of ways to do this. We'll cover
#one that can be done using only what we've covered so far,
#but there are other ways to do this.
#
#First, we start with the function header:

def average_word_length(my_string):
    
    #And as before, we wrap everything in a try block so
    #that we can react to errors that arise:
    try:
        
        #Average word length is the number of characters
        #divided by the number of words. So, we know we're
        #going to need to count both of those things:
        
        word_count = 0
        letter_count = 0
        
        #And we're going to need to reuse the method we used
        #before to avoid consecutive spaces. Notice, though,
        #that this problem says not to assume the string
        #starts with a letter. How can we take care of that?
        #Here, we're going to redefine how we identify words:
        #a new word starts when a letter occurs after a
        #space. So, let's pretend like a space occurred right
        #before the string started:
        
        previous_was_space = True
        
        #This way, if the first character in the string is a
        #letter, it's counted as a new word because it
        #"follows" the space. If it's not, it won't count
        #anyway.
        #
        #Now we iterate through each character in the string:
        
        for letter in my_string:
            
            #For each one, we want to check if it's actually
            #a character we should count. We should count it
            #as a letter if it's a letter. Remember, we only
            #have to worry about not counting spaces and four
            #punctuation marks: .,?!
            
            if not letter == " " and not letter == "." and not letter == "," and not letter == "!" and not letter == "?":
                
                #If this current character isn't any of those
                #characters, we count it as a letter:
                letter_count += 1
                
                #And if it's a letter that occurred after a
                #space, we also note that we found a new
                #word!
                if previous_was_space:
                    word_count += 1
                    
            #Then last, we update previous_was_space based on
            #whether or not this character was a space.
            previous_was_space = letter == " "
            
        #Then, we return the number of letters divided by the
        #number of words.
        return letter_count / word_count
    
    #There are two problems that could arise. One, word_count
    #could have been 0. That means there were no words in the
    #string. So, we catch the ZeroDivisionError and return the
    #string "No words".
    
    except ZeroDivisionError:
        return "No words"
    
    #Or, my_string might not have been a string in the first
    #place. So, we catch a TypeError and return the string
    #"Not a string".
    
    except TypeError:
        return "Not a string"
    
#There are lots of other ways we could have done this. If this
#is confusing to follow, try to revise it so that we count the
#characters and words in the string separately. You could even
#write three functions instead of just one: you could write
#separate functions for word_count and letter_count, and just
#have the original average_word_length function return
#letter_count(my_string) / word_count(my_string).




print(average_word_length("Hi"))
print(average_word_length("Hi, Lucy"))
print(average_word_length("   What   big spaces  you    have!"))
print(average_word_length(True))
print(average_word_length("?!?!?! ... !"))
print(average_word_length("Xrc   VZKSV"))