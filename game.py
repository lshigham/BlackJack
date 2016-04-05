# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 01:10:19 2016

@author: Stew
"""

# Games -- Module Creation

class Player(object):
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score
        
    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep
        
def ask_yes_or_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response
    
def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response
    
    
if __name__ == "__main__":
    print ("You ran this module directly (and didn't 'import' it).")
    input("\n\nPress the enter key to exit.")
    