cafe = "Octane"
balance = 7.5

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Atlanta is full of great coffee places. Unfortunately, great
#coffee is usually expensive. The variables above will
#contain a balance and a cafe name. Below are the prices of
#a cup of coffee at each of three locations:
#
# - Octane: $6
# - Galloway: $5
# - Starbucks: $4
# - Revelator: $3
# - Dunkin: $2
#
#Add some code above that will print one of the following
#two messages depending on whether the value of balance is
#high enough to buy a cup of coffee at the given cafe.
#
# - If it is sufficient, print "With [balance] dollars, I
#   can buy coffee at [cafe]"
# - If it is not sufficient, print "With [balance] dollars,
#   I cannot buy coffee at [cafe]"


#Add your code here!

a= ["Octane", 6]
b= ["Galloway", 5]
c= ["Starbucks", 4]
d= ["Revelator", 3]
e= ["Dunkin", 2]

x= [cafe, 6]

if cafe == e[0]:    
    if balance >= e[1]:
        x = e        
else: 
    if cafe == d[0]:    
        if balance >= d[1]:
            x = d
    else: 
        if cafe == c[0]:    
            if balance >= c[1]:
                x = c
        else: 
            if cafe == b[0]:    
                if balance >= b[1]:
                    x = b
            else: 
                if cafe == a[0]:    
                    if balance >= a[1]:
                        x = a

if balance >= x[1]:
    print("With", balance, "dollars,", "I can buy coffee at", x[0])
else:
    print("With", balance, "dollars,", "I cannot buy coffee at", x[0])