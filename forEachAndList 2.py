liste_de_nombres= [91,92,93,94,95,96,97,98,99,100]
somme= 0

for i in range(0, len(liste_de_nombres)):
    nombre_en_cour= liste_de_nombres[i]
    somme += nombre_en_cour
    
moyenne= somme / len(liste_de_nombres)
print(moyenne)