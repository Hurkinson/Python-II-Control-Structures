entered = "abc123"
password = "abc33"
tries = 1

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Above we've created three variables representing an attempt
#to enter a password. Add some code below that will print the
#result of this check:
#
# - "Login successful." if entered is the same as password
#   and tries is less than or equal to 3.
# - "Incorrect password." if entered is not the same as 
#   password, but tries is less than or equal to 3.
# - "Tries exceeded." if tries is greater than 3.
#
#You don't need to worry about incrementing tries if the
#password is incorrect.


#Add your code here!

if entered is not password: 
       
    if tries >= 4:
        print("Tries exceeded.")            
    if tries <=3:    
        print("Incorrect password.")
        
else: 
    if tries >= 4:
        print("Tries exceeded.")            
    if tries <=3:    
        print("Login successful.")


'''if entered is not password:
    while tries > 0:            
        if tries >= 4:
            print("Tries exceeded.")
            break
        if tries <=3:    
            print("Incorrect password.")
            tries += 1
        if tries >= 3:
            break
else: print("Login successful.")'''
    