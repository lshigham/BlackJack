# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 23:49:00 2016

@author: Stew
"""

# Blackjack!

# Create Card Class
class Card(object):
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]
    
    def __init__(self, rank, suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up
        
    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else: 
            rep = "XX"
        return rep
        
    def flip(self):
        self.is_face_up = not self.is_face_up

# Create Hand CLass
class Hand(object):
    def __init__(self):
        self.cards = []
        
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "  "
        else:
            rep = "<empty>"
        return rep
        
    def clear(self):
        self.cards = []
        
    def add(self, card):
        self.cards.append(card)
        
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
        
        
# Create Deck Class -- This class is based of the "Hand class"
class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))
                
    def shuffle(self):
        import random
        random.shuffle(self.cards)
        
    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't continue deal.  I'm out of cards!")
        
if __name__ == "__main__":
    print("This is a module with classes for playing cards.")  
    input("\n\nPress the enter key to exit.")

# Main - Deck1 dealer
deck1 = Deck()
deck1.populate()
deck1.shuffle()

#Create two Hand objects --assigned to hands:
my_hand = Hand()
your_hand = Hand()
Hands = [my_hand, your_hand]

