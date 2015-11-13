# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 16:31:54 2014
@author: Enbody
"""
import proj11, turtle
    
turtle.speed(10)       
G = proj11.Tic_tac_toe()
G.draw()
index = int(input("Your turn, choose 1-9: "))
while 1 <= index <= 9:
    if not G.set_mark('X',index): # occupied
        index = int(input("Error occupied , choose 1-9: "))
        continue
    if G.determine_winner() == 'X':
        print("You won!")
        break
    if G.full_board(): # only 'X' can fill the board
        print("Full board.")
        break
    proj11.computer_play(G)
    if G.determine_winner() == 'O':
        print("Computer won.")
        break
    G.draw()
    index = int(input("Your turn, choose 1-9: "))
G.draw()
print("Game over.")
    

