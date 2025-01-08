# For the value or rank to compare cards we need to create a dictionary via which can compare their ranks 
import random
Values = {"Two": 2 , 'Three': 3 , 'Four': 4 ,'Five': 5 , 'Six': 6 ,'Seven': 7 ,'Eight': 8 ,'Nine': 9 , 'Ten': 10 ,'Jack': 11 , 'Queen': 12 , 'king': 13 , 'Ace': 14}
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','king','Ace')

# This Class is for setting rank and suits

class card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.Value = Values[rank]
    
    def __str__(self):
        return self.rank + "of" + self.suit

# This Class is for generating all Decks

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # Now This will create card object
                created_card = card(suit,rank)
                self.all_cards.append(created_card)

    # This method shuffle all the generated cards
    def shuffle(self):
        random.shuffle(self.all_cards)

    # This will remove one card from the all cards
    def deal_one(self):
        return self.all_cards.pop()

# Player Class

class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if isinstance(new_cards, list):
            # List of multiple cards objects
            self.all_cards.extend(new_cards)

        else:
            # For Single card object 
            self.all_cards.append(new_cards)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
 
# Game Setup

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for _ in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player One has no cards left! Player Two Wins!!!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two has no cards left! Player One Wins!!!")
        game_on = False
        break

    player_one_cards = [player_one.remove_one()]
    player_two_cards = [player_two.remove_one()]



# This is for main WAR

    at_war = True

    while at_war:
        if player_one_cards[-1].Value > player_two_cards[-1].Value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].Value < player_two_cards[-1].Value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            print("WAR!!")
            if len(player_one.all_cards) < 5:
                print("Player One unable to declare WAR. Player Two Wins!!!")
                game_on = False
                break

            if len(player_two.all_cards) < 5:
                print("Player Two unable to declare WAR. Player One Wins!!!")
                game_on = False
                break

            for _ in range(3):
                if len(player_one.all_cards) > 0:
                    player_one_cards.append(player_one.remove_one())
                if len(player_two.all_cards) > 0:
                    player_two_cards.append(player_two.remove_one())

