
import cards

# Create the deck of cards
def build_deck():
        '''create deck of cards and then split deck into two player decks'''
        the_deck = cards.Deck()
        the_deck.shuffle()
        the_deck.display()
        player1_lst = []
        player2_lst = []
        print("Welcome to War")
        for i in range(26):
                player1_lst.append(the_deck.deal())
                player2_lst.append(the_deck.deal())
        print(player1_lst, " and " , len(player1_lst))
        print(player2_lst, " and " , len(player2_lst))
        print("Deck has been split")
        return (player1_lst,player2_lst)

def compare_cards(card1,card2):
    '''compares the two cards rank, accepts two card obj
    prints out comparisons'''
    win = 0
    print("Player 1's card was ",card1,"and player 2's card was ",card2)
    p1 = card1.get_rank()
    p2 = card2.get_rank()
    print(p1)
    if(p1==1):
        p1 = 14
    if(p2==1):
        p2 = 14
    if p1 == p2:
        win = 0
        print( "Players 1 card ", card1, "and Player2's " \
        "card ", card2," are of of equal rank" )
    elif p1 > p2:
        win = 1
        print( card1, "of higher rank than", card2 )
    else:
        win = 2
        print( card2, "of higher rank than", card1 )
    return win
def battles(player1_lst,player2_lst):
        count = 0
        resume = ""
        print("battle will begin")
        while(resume!="quit"):
                if(len(player1_lst)==52):
                        print("Player 1 wins")
                        break
                elif(len(player2_lst)==52):
                        print("Player 2 wins")
                        break
                else:
                        print("starting battle")            
                        resume = input("Enter quit or press enter to continue")
                        if(resume==""):
                                win = compare_cards(player1_lst[count],\
                                player2_lst[count])
                                if(win==1):
                                        player1_lst.append(player2_lst[count])
                                        player1_lst.append(player1_lst[count])
                                        player1_lst.remove(player1_lst[count])
                                        player2_lst.remove(player2_lst[count])
                                elif(win==2):
                                        player2_lst.append(player1_lst[count])
                                        player2_lst.append(player2_lst[count])
                                        player2_lst.remove(player2_lst[count])
                                        player1_lst.remove(player1_lst[count])
                                elif(win==0):
                                        player1_lst.append(player1_lst[count])
                                        player1_lst.remove(player1_lst[count])
                                        player2_lst.append(player2_lst[count])
                                        player2_lst.remove(player2_lst[count])


                        
def main():
        player1,player2 = build_deck()
        battles(player1,player2)


main()



