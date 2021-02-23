from enum import *
from random import *

full_deck = []
partial_deck = []
ankit_cards = []
parteek_cards = []

#Card enum for playing cards
class Card(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

#Suit emun for playing cards
class Suit(Enum):
    SPADES = 'spades'
    CLUBS = 'clubs'
    HEARTS = 'hearts'
    DIAMONDS = 'diaminds'
#class to hold information for playing cards
class playingcard:
    def __init__(self,card_value, card_suit):
        self.card = card_value
        self.suit = card_suit

#function to deal full deck of cards
def create_deck():
    for suit in Suit:
        for card in Card:
            full_deck.append(playingcard(Card(card), Suit(suit)))
    return full_deck

#Draw single card from "Deck"
def draw_card(deck):
    rand_card = randint(0, len(deck)-1)
    return deck.pop(rand_card)

#deal two players for the game
def deal_war():
    while(len(partial_deck) > 0):
        ankit_cards.append(draw_card(partial_deck))
        parteek_cards.append(draw_card(partial_deck))

create_deck()
partial_deck = list(full_deck)
deal_war()

for i in range(0, len(ankit_cards)):
    if(ankit_cards[i].card > parteek_cards[i].card):
        print("Ankit Wins: ", ankit_cards[i].card)
        print("Parteek Loses: ", parteek_cards[i].card)
    if (ankit_cards[i].card < parteek_cards[i].card):
        print("Parteek Wins: ", parteek_cards[i].card)
        print("Ankit loses: ", ankit_cards[i].card)
    else:
        print("Draw")



