mystery_string = "Lucy"

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#There's an easy way to do this exercise, and a hard way. For
#a hint on the easier way, revisit the sample answers for the
#previous coding exercise.
#
#Above we've created a variable called mystery_string. Write
#some code that will print the first letter of the string on
#the first line, the first two letters on the second line,
#the first three letters on the third line, etc., until it
#prints the entire string on the last line.
#
#For example, if the string was "Lucy", then the output would
#be:
#
#L
#Lu
#Luc
#Lucy
#
#Hint: to print without automatically starting a new line,
#include the text end="" inside the print statement's
#parentheses. For example, print("Hello", end="") will print
#the word "Hello" without starting a new line afterward. So,
#calling it twice would print "HelloHello" on one line
#instead of two lines.


#Add your code here!
count = 1

for i in range(1,len(mystery_string)+1):
    print(mystery_string[0:count])
    count+=1
        
print()  

#----------------------------------------------------------------
import itertools
count = itertools.count(1)

for i in range(1,len(mystery_string)+1):
    print(mystery_string[0:next(count)])
        
print()

#----------------------------------------------------------------

current_row = ""
for letter in mystery_string:
    current_row += letter
    print(current_row)
    
#----------------------------------------------------------------

for i in range(1, len(mystery_string) + 1):
    print(mystery_string[0:i])
    
#----------------------------------------------------------------

current_total_letters = 1
for letter1 in mystery_string:
    current_printed_letters = 0
    for letter2 in mystery_string:
        if current_printed_letters < current_total_letters:
            print(letter2, end="")
            current_printed_letters += 1
    print()
    current_total_letters += 1