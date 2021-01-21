num = 5

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#Write some code below that will print the factorial of num.
#Remember to remove any debug statements when you're ready
#to submit for credit.

result = num
num2 = num
for i in range(num-1):
    print(i, result)
    result *= num2-1
    num2 -=1
print(result)