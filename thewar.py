# imports
import inquirer
import random

# Define suits of the cards
card_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Define values of the cards
card_values = dict(
    two = 2,
    three = 3,
    four = 4,
    five = 5,
    six = 6,
    seven = 7,
    eight = 8,
    nine = 9,
    ten = 10,
    jack = 11,
    queen = 12,
    king = 13,
    ace = 14
)

# Create class to hold information about playing cards
class PlayingCard():
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

# Create full_deck and small_deck to be used dependant on the chosen lenght of the game
full_deck = []
for suit in card_suits:
    for card in card_values:
        full_deck.append(PlayingCard(card, suit))

small_deck = []
for suit in card_suits:
        for card in card_values:
            if card_values[card] >= 9:
                small_deck.append(PlayingCard(card, suit))

# Shuffle chosen deck and deal cards to the players
game_deck = small_deck[:]

random.shuffle(game_deck)

cut = int(len(game_deck) / 2)

p1_deck = game_deck[:cut]
p2_deck = game_deck[cut:]

p1_collected_stack = []
p2_collected_stack = []

def play():
    
    global p1_deck
    global p2_deck
    global p1_collected_stack
    global p2_collected_stack

    if len(p1_deck) == 0:
        p1_deck = p1_collected_stack
        p1_collected_stack = []
        p1_played_card = p1_deck.pop()
    elif len(p1_deck) == 0 and len(p1_collected_stack) == 0:
        print('Game over, player 2 won.')
    else:
        p1_played_card = p1_deck.pop()
    if len(p2_deck) == 0:
        p2_deck = p2_collected_stack
        p2_collected_stack = []
        p2_played_card = p2_deck.pop()
    elif len(p2_deck) == 0 and len(p2_collected_stack) == 0:
        print('Game over, player 1 won.')    
    else:
        p2_played_card = p2_deck.pop()

    if card_values[p1_played_card.value] > card_values[p2_played_card.value]:
        print(f"Player 1 wins the hand with {p1_played_card.value} of {p1_played_card.suit}.")
        print(f"Player 2 lost the hand with {p2_played_card.value} of {p2_played_card.suit}.")
        p1_collected_stack.append(p1_played_card)
        p1_collected_stack.append(p2_played_card)
        print(f"Player 1 stack: {len(p1_deck)}.")
        print(f"Player 1 collected stack: {len(p1_collected_stack)}.")
        print(f"Player 2 stack: {len(p2_deck)}.")
        print(f"Player 2 collected stack: {len(p2_collected_stack)}.")
    elif card_values[p1_played_card.value] < card_values[p2_played_card.value]:
        print(f"Player 2 wins the hand with {p2_played_card.value} of {p2_played_card.suit}.")
        print(f"Player 1 lost the hand with {p1_played_card.value} of {p1_played_card.suit}.")        
        p2_collected_stack.append(p2_played_card)
        p2_collected_stack.append(p1_played_card)
        print(f"Player 1 stack: {len(p1_deck)}.")
        print(f"Player 1 collected stack: {len(p1_collected_stack)}.")
        print(f"Player 2 stack: {len(p2_deck)}.")
        print(f"Player 2 collected stack: {len(p2_collected_stack)}.")
    else:
        print("The WAR!")
        if len(p1_deck) == 0:
            p1_deck = p1_collected_stack
            p1_collected_stack = []
            p1_flipped_card = p1_deck.pop()
        elif len(p1_deck) == 0 and len(p1_collected_stack) == 0:
            print('Game over, player 2 won.')
        else:
            p1_flipped_card = p1_deck.pop()

        if len(p2_deck) == 0:
            p2_deck = p2_collected_stack
            p2_collected_stack = []
            p2_flipped_card = p2_deck.pop()
        elif len(p2_deck) == 0 and len(p2_collected_stack) == 0:
            print('Game over, player 1 won.')    
        else:
            p2_flipped_card = p2_deck.pop()

        if len(p1_deck) == 0:
            p1_deck = p1_collected_stack
            p1_collected_stack = []
            p1_played_card = p1_deck.pop()
        elif len(p1_deck) == 0 and len(p1_collected_stack) == 0:
            print('Game over, player 2 won.')
        else:
            p1_played_card = p1_deck.pop()
        if len(p2_deck) == 0:
            p2_deck = p2_collected_stack
            p2_collected_stack = []
            p2_played_card = p2_deck.pop()
        elif len(p2_deck) == 0 and len(p2_collected_stack) == 0:
            print('Game over, player 1 won.')    
        else:
            p2_played_card = p2_deck.pop()

        if card_values[p1_played_card.value] > card_values[p2_played_card.value]:
            print(f"Player 1 wins the hand with {p1_played_card.value} of {p1_played_card.suit}.")
            print(f"Player 2 lost the hand with {p2_played_card.value} of {p2_played_card.suit}.")
            p1_collected_stack.append(p1_played_card)
            p1_collected_stack.append(p2_played_card)
            p1_collected_stack.append(p1_flipped_card)
            p1_collected_stack.append(p2_flipped_card)
            print(f"Player 1 stack: {len(p1_deck)}.")
            print(f"Player 1 collected stack: {len(p1_collected_stack)}.")
            print(f"Player 2 stack: {len(p2_deck)}.")
            print(f"Player 2 collected stack: {len(p2_collected_stack)}.")
        elif card_values[p1_played_card.value] < card_values[p2_played_card.value]:
            print(f"Player 2 wins the hand with {p2_played_card.value} of {p2_played_card.suit}.")
            print(f"Player 1 lost the hand with {p1_played_card.value} of {p1_played_card.suit}.")        
            p2_collected_stack.append(p2_played_card)
            p2_collected_stack.append(p1_played_card)
            p2_collected_stack.append(p2_flipped_card)
            p2_collected_stack.append(p1_flipped_card)
            print(f"Player 1 stack: {len(p1_deck)}.")
            print(f"Player 1 collected stack: {len(p1_collected_stack)}.")
            print(f"Player 2 stack: {len(p2_deck)}.")
            print(f"Player 2 collected stack: {len(p2_collected_stack)}.")
        else:
            print(f"Player 1 stack: {len(p1_deck)}.")
            print(f"Player 1 collected stack: {len(p1_collected_stack)}.")
            print(f"Player 2 stack: {len(p2_deck)}.")
            print(f"Player 2 collected stack: {len(p2_collected_stack)}.") 
        print(f"Player 1 stack: {len(p1_deck)}.")
        print(f"Player 1 collected stack: {len(p1_collected_stack)}.")
        print(f"Player 2 stack: {len(p2_deck)}.")
        print(f"Player 2 collected stack: {len(p2_collected_stack)}.")