# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:29:10 2020

@author: Hurkinson
"""

print(" trouve un mot à faire deviner:")
guess = input()
guessL = list(guess)
guessed = ""
print(" maintenant, chois une lettre !")


while not guessed == guessL:
    try1 = input()
    if try1 in guess:
        print(" il y a bien un ", try1, "dans le mot a deviner")
        guessed ="try1)
        guessed.sort()
        print(guessed)

