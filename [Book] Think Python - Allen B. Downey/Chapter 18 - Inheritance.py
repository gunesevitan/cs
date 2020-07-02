# Chapter Eighteen Exercises



import random

def cmp(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    elif x == y:
        return 0


class Card:
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8',
        '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __cmp__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res=[]
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def shuffle(self):
        random.shuffle(self.cards)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def sort(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hands(self, hands, cards):
        created_hands = []
        for i in range(hands):
            created_hands.append(Hand(str(i)))  # Creates hands and stores in a list

        for c in range(cards):
            for hand in created_hands:
                hand.add_card(self.pop_card())  # Adding cards to hand one by one from the deck




class Hand(Deck):
    def __init__(self, label=''):
        super().__init__()
        self.cards = []
        self.label = label



# Exercise 18.1
# Write a __cmp__ method for Time objects. Hint: you can use tuple comparison, but you
# also might consider using integer subtraction.



def __cmp__(self, other):
    return cmp(self.time_to_int() - other.time_to_int())



# Exercise 18.2
# Write a Deck method named sort that uses the list method sort to sort the cards in a
# Deck. sort uses the __cmp__ method we defined to determine sort order.



def sort(self):
    self.cards.sort()



# Exercise 18.3
# Write a Deck method called deal_hands that takes two parameters, the number of hands
# and the number of cards per hand, and that creates new Hand objects, deals the appropriate
# number of cards per hand, and returns a list of Hand objects.



def deal_hands(self, hands, cards):
    created_hands = []
    for i in range(hands):
        created_hands.append(Hand(str(i)))  # Creates hands and stores in a list

    for c in range(cards):
        for hand in created_hands:
            hand.add_card(self.pop_card())  # Adding cards to hand one by one from the deck



# Exercise 18.4
# Read TurtleWorld.pyi World.py and Gui.py and draw a class diagram that shows the
# relationships among the classes defined there.



# Gui is class.
class Gui:
    pass

# World is class and inherits from Gui.
class World(Gui):
    pass

# TurtleWorld is a class and inherits from World, which inherits from Gui.
class TurtleWorld(World):
    pass

# TurtleWorld --> World --> Gui



# Exercise 18.5
# Download my code from "Markov Analysis" and follow the steps described above to
# encapsulate the global variables as attributes of a new class called Markov.



from random import choice


class Markov(object):

    def __init__(self):
        self.suffix_map = {}
        self.prefix = ()

    def process_file(self, filename, order=2):
        file_pointer = open(filename)
        self.skip_header(file_pointer)  # Skipping the header with defined function in 13.2

        for line in file_pointer:
            for word in line.rstrip().split():
                self.process_word(word, order)

    def skip_header(self, file_pointer):
        for line in file_pointer:
            if line.startswith('Produced by'):
                break

    def process_word(self, word, order=2):
        if len(self.prefix) < order:
            self.prefix += (word,)
            return

        try:
            self.suffix_map[self.prefix].append(word)  # Appending the word to the suffix list mapped to a prefix
        except KeyError:
            self.suffix_map[self.prefix] = [word]  # If prefix doesn't exist, creating it

        self.prefix = shift(self.prefix, word)

    def random_text(self, num_words):
        start = choice(self.suffix_map.keys())

        for i in range(num_words):
            suffixes = self.suffix_map.get(start, None)
            if suffixes == None:
                self.random_text(num_words - i)
                return


            word = choice(suffixes)  # Choosing a random suffix
            start = shift(start, word)


def shift(t, word):
    return t[1:] + (word,)  # Removing tuples first word and adding the given word to the end