import itertools



def addict(item):        # itertools necessaire
    final= {}
    mot= "mot_"
    n = next(itertools.count(1))
    final[mot+str(n)] = item
    
    return final
  





test= addict(12), addict("zizi")

print(test)


'''>>> dico = {}
>>> var = "var_"
>>> def fonction(n, value):
...     dico[var+str(n)] = value
...
>>> fonction(1, 15)
>>> fonction(2, 10)
>>> dico
{'var_2': 10, 'var_1': 15}
>>>
>>> for i in range(10, 20):
...     fonction(i, i*2)
...
>>> dico
{'var_17': 34, 'var_16': 32, 'var_15': 30, 'var_14': 28, 'var_13': 26, 'var_12': 24, 'var_11': 22, 'var_10': 20, 'var_19': 38, 'var_18': 36, 'var_2': 10, 'var_1': 15}'''