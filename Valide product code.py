#Imagine you're writing the software for an inventory system for
#a store. Part of the software needs to check to see if inputted
#product codes are valid.
#
#A product code is valid if all of the following conditions are
#true:
#
# - The length of the product code is a multiple of 4. It could
#   be 4, 8, 12, 16, 20, etc. characters long.
# - Every character in the product code is either an uppercase
#   character or a numeral. No lowercase letters or punctuation
#   marks are permitted.
# - The character sequence "A1" appears somewhere in the
#   product code.
#
#Write a function called valid_product_code. valid_product_code
#should have one parameter, a string. It should return True if
#the string is a valid product code, and False if it is not.


#Add your code here!
def valid_product_code(a_str):
    valid = []
    if len(a_str)%4 ==0:
        if "A1" in a_str:
            #print(len(a_str), "char in str")
            for c in a_str:
                #print(ord(c))
                if ord(c) in range(65,91) or ord(c) in range(48,58):
                    valid.append("True")
                    
                else:
                    valid.append("False")
                    
        else:
            #print("No A1 in str")
            valid.append("False")
    else:
        #print("longueur incorrecte")
        valid.append("False")    
    #print (valid)    
    if "False" in valid:
        return False
    else:
        return True
        
    
#Remember, capital letters have ordinal numbers between 65
#("A") and 90 ("Z"). You may use the ord() function to get
#a letter's ordinal number.

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: True, True, False, False, False
print(valid_product_code("A12B44BP"))
print(valid_product_code("BFDSAUSA98932RWEFOEWA9FEAA1DSFSF"))
print(valid_product_code("A1BBD5"))
print(valid_product_code("BDD5664S"))
print(valid_product_code("66aBSaA1fdsv"))
print(valid_product_code("BFDSAUSA98932RWEFOEWA9FEAA1DSFSF"))
