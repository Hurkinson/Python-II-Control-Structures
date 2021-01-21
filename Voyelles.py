#Write a function called has_a_vowel. has_a_vowel should have
#one parameter, a string. It should return True if the string
#has any vowels in it, False if it does not.


def has_a_vowel(a_str):
    result= ""
    voyelles = "aeiou"
    #print("Starting...")
    try:
        if a_str == "":
            #print("il n'y pas de lettres dans la proposition")
            result = "False"     
        for letter in a_str:
            #print("Checking", letter)
            if letter in voyelles:
                #print(letter, "is a vowel, returning True")
                result += "True"
            else:     
                #print(letter, "is not a vowel, returning False")
                result += "False"
                
    except Exception as error:
                print(error)
                
                               
    finally:
        #print(result)
        #print("Done!")
        if "True" in result:
            return True
        else:
            return False
        
    
    
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, then True, then False, then False, each on
#its own line.
print(has_a_vowel("abba"))
print(has_a_vowel("beeswax"))
print(has_a_vowel("syzygy"))
print(has_a_vowel(""))


#-----------------------------------------------------------
#When most people try to solve this, they do one of two
#things: they either return inside the loop (terminating the
#function early) or they try to wait until the end to return.
#The latter can work, but the logic is somewhat tough to
#pull off.
#
#Fortunately, there is an easier way. Once you find a vowel,
#you can return True -- you only need to find one for the
#result to be True. So, let's write that part:

def has_a_vowel(a_str):
    for letter in a_str:
        if letter in "aeiou":
            return True
        
    #That's all what we had before, which is fine... but
    #we weren't having a problem returning True. Our problem
    #was returning False.
    #
    #But let's think for a second: if a vowel was found, then
    #the return statement ran. That kills the function. There
    #is no way the next line can run if a vowel was already
    #found... so the only way it can run is if no vowel was
    #found... which means we can go ahead and:
    return False
    
    #This takes care of our None issue as well. Before, None
    #was returned for empty strings because the only returns
    #were inside the loop, which required a non-empty string
    #to do anything. Now, it returns False whenever it hasn't
    #met the conditions to return True.