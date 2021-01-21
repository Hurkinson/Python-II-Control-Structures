#Recall Coding Problem 2.4.4. In that problem, you calculated
#the damage done by an attack based on several parameters.
#
#Convert your code from there into two functions, one called
#calculate_damage and one called calculate_modifier.
#
#Your function for calculate_damage must call calculate_modifier;
#it may not calculate the modifier separately. As such,
#calculate_damage should accept all ten parameters: STAB,
#Type, Critical, Other, Random, Level, Attack, Defense, and
#Base. You'll need to pass STAB, Type, Critical, Other, and
#Random to calculate_modifier.
#
#Make sure the parameters to each function follow the order
#shown above.
#
#As a reminder, damage is calculated using this formula:
#https://studio.edx.org/asset-v1:GTx+CS1301+1T2017+type@asset+block@DamageCalc.png
#
#Modifier is calculated using this formula:
#https://studio.edx.org/asset-v1:GTx+CS1301+1T2017+type@asset+block@ModifierCalc.png


#Add your code here!
def calculate_modifier(STAB, Type, Critical, Other, Random):
    modifier = STAB * Type * Critical * Other * Random
    return modifier

def calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack, Defense, Base):

    df1 = ((2*Level+10)/250)
    df2 = (Attack/Defense)
    df3 = Base

    Damage = (df1 * df2 * df3 +2)* calculate_modifier(STAB, Type, Critical, Other, Random)
    return Damage

#Below are some lines of code that will test your function.
#You can change the value of the variable to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 16.0
STAB = 1
Type = 0.25
Critical = 2
Other = 1
Random = 1
Level = 50
Attack = 125
Defense = 110
Base = 60

print(calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack, Defense, Base))

#------------------------------------------------------------------------------------------

#calculate_modifier is relatively straightforward: there are five
#parameters, and we just return the product of all five:

def calculate_modifier(STAB, Type, Critical, Other, Random):
    return STAB*Type*Critical*Other*Random

#Once we have that, we can work on calculate_damage. First, we
#declare the formula. Because it's going to call calculate_modifier,
#it needs to have *all* the parameters, including the ones it's
#going to send to calculate_modifier. After all, it can't send
#them if it doesn't have them!

def calculate_damage(STAB, Type, Critical, Other, Random, Level, Attack, Defense, Base):
    
    #There are lots of ways to do this next part. For me, I find
    #it easiest to first calclate the part of the formula that does
    #not rely on the modifier:
    
    initial_damage = ((2 * Level + 10) / 250) * (Attack / Defense) * Base + 2
    
    #Then, I retrieve the modifier:
    
    modifier = calculate_modifier(STAB, Type, Critical, Other, Random)
    
    #Then, I return the product of the two:
    
    return initial_damage * modifier
    
    #You could do this lots of other ways, though. You could do it all on one
    #line, or break the formula from line 19 into multiple sub-stages.
    

