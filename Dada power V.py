def get_integer(my_var):
    if isinstance(my_var,tuple):
        raise Exception("impossible de convertir un tuple en entier")
    try:
        return int(my_var)
    except: #Exception as error:
        print("Cannot convert!")
        raise
    finally:
        print('en tout cas on a bien lancé la fonction')
    
print(get_integer("5"))
print(get_integer("Boggle."))
print(get_integer(5.1))


