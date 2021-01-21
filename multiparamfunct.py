#Defines the function "currencyAmount"
def currencyAmount(currency, amount): 
    if currency == "JPY":
        return "¥" + str(amount)
    elif currency == "USD":
        return "$" + str(amount)
    elif currency == "GBP":
        return "£" + str(amount)
    else:
        return str(amount)

#Prints the output of currencyAmount("GBP", 5)
print(currencyAmount("GBP", 5))    
