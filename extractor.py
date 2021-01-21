mystery_string = "my cat your cat"
mot_a_chercher='your'
import itertools

def extractor(target,string):
    n = itertools.count(1)
    size= len(target)    
    m= []
    for c in string:
        #print(c)
        if c == target[0]:
            print(target[0])
            print(string[string.index(c):(string.index(c)+size)])
            if string[string.index(c):(string.index(c)+size)] == target:
                m.append(c)
                m.append(string.index(c))
                print("zizi!")
        else:
            continue
            
            
        '''elif c == target[next(n)]:
            m.append(c)
            m.append(string.index(c))
            
        elif c == target[next(n)]:
            m.append(c)
            m.append(string.index(c))
            if string.index(c)+1 == target[1]:
               m.append(c+1)
               m.append(string.index(c)+1)''' 
    return m
            

print(extractor(mot_a_chercher, mystery_string))