import cards
#####################
#Build a deck of cards and play the game of blackjack according
#to the specifications

# Create the deck of cards
def build_deck():
        '''create deck of cards and then split deck into two player decks'''
        the_deck = cards.Deck()
        the_deck.shuffle()
        the_deck.display()
        return the_deck
def calc_hand(hand):
    '''accepts list of cards values in hand, calculates sum, returns sum'''
    return sum(hand)
def blackjack(deck):
    '''accept a deck object, take user input to play and
        use the given AI for the dealer, print out results after each
        round and the game'''
    play = ""
    wins = 0
    losses = 0
    ties = 0
    #makes sure deck isn't empty
    while(len(deck)>0):
            #loops until player doesn't want to play anymore
            while(play=="y" or play==""):
                resume = ""
                #initializing lists of hands and values in their hands
                player_hand = []
                dealer_hand = []
                player_values = []
                dealer_values =[]
                #first two cards for player/dealer
                for x in range(2):
                    player_hand.append(deck.deal())
                    dealer_hand.append(deck.deal())
                for x in range(len(player_hand)):
                    player_values.append(int(player_hand[x].get_value()))
                #adding values
                for x in range(len(dealer_hand)):
                    dealer_values.append(int(dealer_hand[x].get_value()))
                print("Player: ", end = "")
                for x in player_hand:
                        print(x, " ", end="")
                print("; highest value is ",calc_hand(player_values))
                print("Dealer: " ,dealer_hand[0] , "X")
                dealer_sum = 0
                p_sum = 0
                outcome = ""
                loss = False
                win = False
                print("Starting round")
                #loops until game is won,lost, or tied
                while((resume=="y" or resume=="" or resume=="h")):
                    p_sum = calc_hand(player_values)
                    #bust check
                    if(p_sum>21):
                        print("Players busts")
                        outcome="busts"
                        losses+=1
                        loss = True
                        break
                    #checks for aces and asks player for value wanted
                    for x in range(0,len(player_hand)):
                            if(player_hand[x].get_value()==1):
                                print("Player: ", end = "")
                                for x in range(len(player_hand)):
                                        print(x, " ", end="")
                                print("; highest value is ",p_sum)
                                print("Max hand would be " , p_sum+10)
                                ace = input("Would you like to make that ace be worth 11 or 1")
                                if(ace=="11"):
                                    player_values[x]=11
                                else:
                                    player_values[x]==1
                    resume = input("Hit 'h' or enter, Stand = any other char")
                    resume.lower()
                    if(resume=="y" or resume=="" or resume=="h"):
                            for x in range(len(player_hand)):      
                                    if(player_hand[x].get_value()==1):
                                            print("Player: ", end = "")
                                            for x in player_hand:
                                                print(x, " ", end="")
                                            print("; highest value is ",p_sum)
                                            print("Max hand would be " , p_sum+10)
                                            ace = input("Would you like to make that ace be worth 11 or 1")
                                            if(ace=="11"):
                                                    player_values[x]=11
                                            else:
                                                    player_values[x]==1
                            player_hand.append(deck.deal())
                            player_values.append(int(player_hand[len(player_hand)-1].get_value()))
                            p_sum = calc_hand(player_values)
                            print("Player: ", end = "")
                            for x in player_hand:
                                print(x, " ", end="")
                            print("; highest value is ",p_sum)
                            for x in range(len(player_hand)):
                                    if(player_hand[x].get_value()==1):
                                            ace = input("Would you like to make that ace be worth 11 or 1")
                                            ace = int(ace)
                                            if(ace==11):
                                                    player_values[x]=11
                                            else:
                                                    player_values[x]==1
                            p_sum = calc_hand(player_values)
                            '''print("Player: ", end = "")
                            for x in player_hand:
                                print(x, " ", end="")
                            print("; highest value is ",p_sum)'''
                    else:
                        break
                if(outcome!="busts"):
                    print("Player stands and his hand is worth", p_sum)
                
                if(loss==False):
                        print("Dealer: ", end = "")
                        for x in dealer_hand:
                                print(x, " ", end="")
                        dealer_sum = calc_hand(dealer_values)
                        while(dealer_sum<17):
                            added = False
                            print()
                            print("Dealer: ", end = "")
                            for x in dealer_hand:
                                print(x, " ", end="")
                            print("; highest value is ",dealer_sum)
                            print()
                            dealer_sum = calc_hand(dealer_values)
                            if(dealer_sum<17):
                                for x in range(len(dealer_hand)):
                                    if(dealer_hand[x].get_value()==1):
                                        if(dealer_sum+10>17 and dealer_sum+10<21):
                                            dealer_values[x] == 11
                                            added = True
                                            break
                                if(added==False):
                                        print("Dealer hits")
                                        dealer_hand.append(deck.deal())
                                        dealer_values.append(int(dealer_hand[len(dealer_hand)-1].get_value()))
                                        dealer_sum = calc_hand(dealer_values)
                                        print()
                                        print("Dealer: ", end = "")
                                        for x in dealer_hand:
                                                print(x, " ", end="")
                                        print("; highest value is ",dealer_sum)
                                        print()
                        else:
                            if(dealer_sum>21):
                                print("Dealer busts")
                                win = True
                                wins+=1
                            else:
                                print("Dealer stands")
                if(win==False and loss==False):
                        if(p_sum>dealer_sum):
                            print("Player beat Dealer")
                            wins+=1
                        elif(p_sum<dealer_sum):
                            print("Dealer wins against Player")
                            losses+=1
                        else:
                            print("Tie")
                            ties+=1
                play = input("Play again?")
                if(play=="Y" or play=="y" or play==""):
                        continue
                else:
                        print("Player won " , wins)
                        print("Player lost " , losses)
                        print("Player tied " , ties)
                        break
    else:
        print("Game is a tie")
        ties+=1
    print("Player won " , wins)
    print("Player lost " , losses)
    print("Player tied " , ties)
def main():
        '''main function, calls to build a deck and then runs the progam'''
        deck = build_deck()
        blackjack(deck)

main()
