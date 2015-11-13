##
## Demonstrate some of the operations of the Deck and Card classes
##

import cards

# Seed the random number generator to a specific value so every execution
# of the program uses the same sequence of random numbers (for testing).

import random


# Create a deck of cards

my_deck = cards.Deck()

def compare_cards(card1,card2):
    '''compares the two cards, suit,rank,and value, accepts two card obj
    prints out comparisons'''
    if card1.get_suit() == card2.get_suit():
        print( card1, "same suit as", card2 )
    else:
        print( card1, "and", card2, "are from different suits" )
    if card1.get_rank() == card2.get_rank():
        print( card1, "and", card2, "of equal rank" )
    elif card1.get_rank() > card2.get_rank():
        print( card1, "of higher rank than", card2 )
    else:
        print( card2, "of higher rank than", card1 )

    if card1.get_value() == card2.get_value():
        print( card1, "and", card2, "of equal value" )
    elif card1.get_value() > card2.get_value():
        print( card1, "of higher value than", card2 )
    else:
        print( card2, "of higher value than", card1 )
# Shuffle the deck, then display it in 13 columns

my_deck.shuffle()
print( "===== shuffled deck =====" )
my_deck.display()


# Deal five cards to each player (alternating)

print( "Dealt five cards to each player (alternating)" )
print()

player1_list=[]
player2_list=[]
for i in range( 5 ):
    player1_list.append( my_deck.deal() )
    player2_list.append( my_deck.deal() )
    if(i!=1):
        if(i!=4):
            print("Player 1's hand is ", player1_list)
            print("Player 2's hand is " , player2_list)
        else:
            print("Player 1 was dealt " , player1_list[i])
            print("Player 2 was dealt " , player2_list[i])
            compare_cards(player1_list[i],player2_list[i])
    elif(i==1):
        print("Player 1 was dealt " , player1_list[i])
        print("Player 2 was dealt " , player2_list[i])
        compare_cards(player1_list[i],player2_list[i])


# Display each player's cards and the cards still in the deck

print( "===== player #1 =====" )
print()
print( player1_list )
print()
print( "===== player #2 =====" )
print()
print( player2_list )
print()
print( "===== remaining cards in deck =====" )
my_deck.display()


# First card dealt to Player #1

player1_card = player1_list.pop( 0 )

print( "First card dealt to player #1:", player1_card )


# First card dealt to Player #2

player2_card = player2_list.pop( 0 )

print( "First card dealt to player #2:", player2_card )


# Compare the two cards using operloaded operators

print()
if player1_card == player2_card:
    print( "Tie:", player1_card, "and", player2_card, "of equal rank" )
elif player1_card > player2_card:
    print( "Player #1 wins:", player1_card, "of higher rank than", player2_card )
else:
    print( "Player #2 wins:", player2_card, "of higher rank than", player1_card )

