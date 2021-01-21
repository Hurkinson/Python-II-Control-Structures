n = 5

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Write some code that will find and print the factorial of
#the number given by n above. You may not import anything
#from the Python math library.
#
#Hint: Use a while loop, but be careful to avoid an infinite
#loop!


#Add your code here!
  
def fact(n):
    
    x=1
    for i in range(2,n+1):
        x*=i
    return x

print(fact(n))