###### Simulate a Game of Tic Tac Toe with a AI for the computer's turn###########

import turtle
turtle.down()
#board = ["","","","","","","","",""]
class Tic_tac_toe(object):
    def __init__(self):
        '''initializes the board,position,and state of board been drawn'''
        print("Tic Tac Toe")
        self.board = ["","","","","","","","",""]
        self.drawn = False
        self.pos = 0
    def draw(self):
        '''draws the playing grid and the ‘X’s and ‘O’s
        that have been played '''
        #draws board if board hasn't been drawn yet
        #else doesn't redraw the board
        if(self.drawn==False):
            #draws board
            A = turtle.pos()
            turtle.forward(300)
            turtle.up()
            turtle.right(90)
            turtle.forward(100)
            turtle.down()
            turtle.right(90)
            turtle.forward(300)
            turtle.right(180)
            turtle.up()
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(100)
            turtle.right(180)
            turtle.down()
            turtle.forward(300)
            turtle.right(90)
            turtle.up()
            turtle.forward(100)
            turtle.down()
            turtle.right(90)
            turtle.forward(300)
            turtle.up()
            turtle.setposition(A)
            turtle.right(180)
            turtle.forward(20)
            turtle.right(90)
            turtle.forward(30)
            turtle.down()
            self.drawn = True
            self.pos = turtle.pos()
            
    def set_mark(self,mark,index):
        '''checks board of (1-9) for a X or O to see if
        a mark has been placed there. 1 = not taken, 0 = taken '''
        spot = index
        if(self.board[index-1]!=""):
            return 0
        #mark hasn't been placed in spot, goes and places the spot
        else:
            print("XX",self.board)
            self.board[spot-1] = mark
            print("board after players move",self.board)
            Draw_mark.draw(index,mark,self.board)
            turtle.setposition(self.pos)
            return 1
    def determine_winner(self):
        '''returns X if player wins, O if computer wins, or None for no-one'''
        #default, returns None if no one wins=unchanged through logic
        winner = None
        #checks horizontal win for player/computer
        mark = "X"
        for x in range(0,2):
            if(self.board[0]==self.board[1] and self.board[1]==self.board[2] and self.board[0]==mark):
                winner = mark
                break
            if(self.board[3]==self.board[4] and self.board[4]==self.board[5] and self.board[3]==mark):
                winner = mark
                break
            if(self.board[6]==self.board[7] and self.board[7]==self.board[8] and self.board[7]==mark):
                winner = mark
                break
            mark = "O"
            
            
            
            
        #checks vertical win for player/computer
        mark = "X"
        for y in range(0,2):
            if(self.board[0]==self.board[3] and self.board[3]==self.board[6] and self.board[0]==mark):
                winner =mark
                break
            if(self.board[1]==self.board[4] and self.board[4]==self.board[7] and self.board[1]==mark):
                winner =mark
                break
            if(self.board[2]==self.board[5] and self.board[5]==self.board[8] and self.board[2]==mark):
                winner =mark
                break
            mark = "O"
        #checks if computer has middle spot, checks player diag win
        if not self.board[4]=="O":
            #diagonal check
            if self.board[0]=="X" and self.board[4]=="X" and self.board[8]=="X":
                winner = "X"
            #other diag check
            elif self.board[2]=="X" and self.board[4]=="X" and self.board[6]=="X":
                winner = "X"
        #check computer diag win
        else:
            if self.board[0]=="O" and self.board[4]=="O" and self.board[8]=="O":
                winner = "O"
            elif self.board[2]=="O" and self.board[4]=="O" and self.board[6]=="O":
                winner = "O"
        return winner

    def full_board(self):
        '''returns True if all 9 slots are full otherwise returns False '''
        full = False
        count = 0
        for x in range(0,8):
            #if any spot is empty, break and return that the board isn't full
            if(self.board[x]==""):
                return False
                break
            else:
                full = True
        return full
#object that does all movement to the square, and then calls method to draw an X or O
class Draw_mark(object):
    '''object that does all movement to the square, and then calls method to draw an X or O'''
    def __init__():
        '''empty initializer'''
        print()
    def draw(spot,mark,board):
        '''movement to square, then calls drawX or drawO, accepts a spot 1-9,the type X or O, and the list
        of board'''
        turtle.up()
        turtle.back(10)
        pos = turtle.pos()
        print(board)
        #checks if first column
        if(spot==1 or spot==4 or spot==7):
            #movement to 2nd row
            if(spot==4):
                turtle.right(90)
                turtle.forward(100)
                turtle.left(90)
                turtle.down()
                #checks type of mark and calls respective draw mark class
                if(mark=="X"):
                    drawX()
                else:
                    drawO()
            #movement to third row
            elif(spot==7):
                turtle.right(90)
                turtle.forward(200)
                turtle.left(90)
                turtle.down()
                if(mark=="X"):
                    drawX()
                else:
                    drawO()
            else:
                if(mark=="X"):
                    drawX()
                else:
                    drawO()
        #moves to 2nd column
        elif(spot==2 or spot==5 or spot==8):
            turtle.forward(100)
            #etc etc etc code for movements and drawing marks
            if(spot==5):
                turtle.right(90)
                turtle.forward(100)
                turtle.left(90)
                turtle.down()
                if(mark=="X"):
                    drawX()
                else:
                    drawO()
            elif(spot==8):
                turtle.right(90)
                turtle.forward(200)
                turtle.left(90)
                turtle.down()
                if(mark=="X"):
                    drawX()
                else:
                    drawO()
            else:
                if(mark=="X"):
                    drawX()
                else:
                    drawO()
        else:
            turtle.forward(200)
            if(spot==6):
                turtle.right(90)
                turtle.forward(100)
                turtle.left(90)
                turtle.down()
                if(mark=="X"):
                    drawX()
                else:
                    drawO()
            elif(spot==9):
                turtle.right(90)
                turtle.forward(200)
                turtle.left(90)
                turtle.down()
                if(mark=="X"):
                    drawX()
                else:
                    drawO()
            else:
                if(mark=="X"):
                    drawX()
                else:
                    drawO()
        turtle.setheading(0)
        turtle.setposition(pos)
        

def drawX():
    '''contains all instructions on how to draw an X'''
    turtle.down()
    turtle.left(45)
    turtle.forward(75)
    turtle.up()
    turtle.right(135)
    turtle.forward(52)
    turtle.down()
    turtle.right(135)
    turtle.forward(75)
    turtle.up()
def drawO():
    '''contains all instructions on how to draw an O'''
    turtle.up()
    x = turtle.pos()
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.down()
    turtle.circle(40)
    turtle.up()
    turtle.setposition(x)
def stuff(game):
    '''not used anymore'''
    for x in range(0,len(game.board)):
        mark = "O"
        if game.board[x]=="":
            print("ABC",game.board)
            print(x)
            game.board[x] = mark
            Draw_mark.draw(x+1,mark,game.board)
            break
            game.board[x] = mark
            Draw_mark.draw(x,mark,game.board)
def computer_play(game):
    '''plays the O or the computer, accepts a tictactoe object'''
    board  = game.board
    #strategy, middle spot = best
    if(board[4]==""):
        game.board[4] = "O"
        Draw_mark.draw(5,"O",game.board)
    #if has 2 in row, takes the win
    elif(tryToWin(board)>0):
        print('abc')
        #corners code
    elif(board[0]==""):
        game.board[0] = "O"
        Draw_mark.draw(1,"O",game.board)
    elif(board[2]==""):
        game.board[2] = "O"
        Draw_mark.draw(3,"O",game.board)
    elif(board[6]==""):
        game.board[6] = "O"
        Draw_mark.draw(7,"O",game.board)
    elif(board[8]==""):
        game.board[8] = "O"
        Draw_mark.draw(9,"O",game.board)
    #takes next open spot
    else:
        for x in range(0,len(game.board)):
            mark = "O"
            if game.board[x]=="":
                print("ABC",game.board)
                print(x)
                game.board[x] = mark
                Draw_mark.draw(x+1,mark,game.board)
                break
                game.board[x] = mark
                Draw_mark.draw(x,mark,game.board)
        print("failed to choose a move")
    print("board after computer", game.board)
    '''elif tryToWin(board):
        print("T")
    elif tryToBlock(board):
        print("X")
    elif blockexception(board):
        print("Z")
    elif pickCorner(board):
        print("D")'''
def tryToWin(board):
    '''takes in the board list, takes the win if two in a row'''
    a = 0
    #loop for win takes horiz/vertical
    y=0
    for x in range(0,3):
        #horizontal win take checks
        if(board[0+x]=="O" and board[1+x]=="O" and board[2+x]==''):
            print("board is ", board)
            board[x+2] = "O"
            print("board was ", board)
            Draw_mark.draw(x+2,"O",board)
            a+=1
        elif(board[0+x]=="O" and board[1+x]=='' and board[2+x]=="O"):
            board[x+1] = "O"
            print("D")
            Draw_mark.draw(x+2,"O",board)
            a+=1
        elif(board[0+x]=="" and board[1+x]=='O' and board[2+x]=='O'):
            board[x] = "O"
            print('zzz')
            Draw_mark.draw(x+1,"O",board)
            a+=1
        #vertical win take checks
        if (board[0+x]=="O" and board[3+x]=="O" and board[6+x+y]==""):
            board[x+y+6] = "O"
            print("B")
            Draw_mark.draw(x+y+7,"O",board)
            a+=1
        elif (board[0+x+y]=="O" and board[3+x+y]=="" and board[6+x+y]=="O"):
            
            board[x+y+3] = "O"
            print("Z")
            Draw_mark.draw(x+y+4,"O",board)
            a+=1
        if (board[0+x+y]=="" and board[3+x+y]=="O" and board[6+x+y]=="O"):
            
            board[x+y] = "O"
            print('asdfasdf')
            Draw_mark.draw(x+y+1,"O",board)
            a+=1
        x+=3
        if(a>0):
            print('this worked')
            return a
        
    #diagonals
    if (board[0]=='O' and    board[4]=='O' and board[8]==' '):
            
            board[8] = "O"
            Draw_mark.draw(8,"O",board)
            return True
    if (board[8]=='O' and    board[4]=='O' and board[0]==' '):
            
            board[0] = "O"
            Draw_mark.draw(0,"O",board)
            return True
    if(board[0]=='O' and board[8]=='O' and    board[4]==' '):
            
            board[4] = "O"
            Draw_mark.draw(4,"O",board)
            return True
    if (board[6]=='O' and    board[4]=='O' and board[2]==' '):
      
            board[2] = "O"
            Draw_mark.draw(2,"O",board)
            return True
    if (board[2]=='O' and    board[4]=='O' and board[6]==' '):
        
            board[6] = "O"
            Draw_mark.draw(6,"O",board)
            return True
    if (board[2]=='O' and board[6]=='O' and    board[4]==' '):
            
            board[4] = "O"
            Draw_mark.draw(4,"O",board)
            return True
    return False
def tryToBlock(board):
  #loops for loss horiz/vert block
  for y in range(0,2):
            for x in range(0,3):
                #horizontal win block
                if (board[0+x]=='X' and board[1+x]=='X' and board[2+x]==''):
                        
                    board[x] = "O"
                    Draw_mark.draw(2+x,"O",board)
                    return True
                elif (board[0+x+y]=='X' and board[1+x+y]=='' and board[2+x+y]=="X"):
                        
                        board[1+x] = "O"
                        Draw_mark.draw(1+x,"O",board)
                        return True
                elif (board[0+x+y]=='' and board[1+x+y]=='X' and board[2+x+y]=='X'):
                        
                        board[x] = "O"
                        Draw_mark.draw(x,"O",board)
                        return True
                #vertical win block
                if (board[0+x+y]=='X' and board[1+x+y]=='X'and board[2+x+y]==""):
                        
                        board[x+2+y] = "O"
                        Draw_mark.draw(x+y+2,"O",board)
                        return True
                elif (board[0+x+y]=='X' and board[1+x+y]==''and board[2+x+y]==' '):
                        
                        board[x+y+1] = "O"
                        Draw_mark.draw(x+y+1,"O",board)
                        return True
                elif (board[0+x+y]=='' and board[1+x+y]=='X' and board[2+x+y]=='X'):
                        
                        board[x+y] = "O"
                        Draw_mark.draw(x+y,"O",board)
                        return True
                return False
  #block win diagonals
  if (board[0]=='X' and    board[4]=='X' and board[8]==' '):
    
    board[8] = "O"
    Draw_mark.draw(8,"O",board)
    return True
  if (board[8]=='X' and    board[4]=='X' and board[0]==' '):
    board[0] = "O"
    Draw_mark.draw(0,"O",board)
    return True
  if(board[0]=='X' and board[8]=='X' and    board[4]==' '):
    board[4] = "O"
    Draw_mark.draw(4,"O",board)
    return True
  if (board[6]=='X' and    board[4]=='X' and board[2]==' '):
    board[2] = "O"
    Draw_mark.draw(2,"O",board)
    return True
  if (board[2]=='X' and    board[4]=='X' and board[6]==' '):
    board[6] = "O"
    Draw_mark.draw(6,"O",board)
    return True
  if (board[2]=='X' and board[6]=='X' and    board[4]==' '):
    board[4] = "O"
    Draw_mark.draw(4,"O",board)
    return True
  return False
def pickCorner(board):
    if(board[0]==' '):
        board[0] = "O"
        Draw_mark.draw(0,"O",board)
        return True
    elif (board[2]==' '):
        board[2] = "O"
        Draw_mark.draw(2,"O",board)
        return True
    elif (board[6]==' '):
        board[6] = "O"
        Draw_mark.draw(6,"O",board)
        return True
    elif(board[8]==' '):
        board[8] = "O"
        Draw_mark.draw(8,"O",board)
        return True
    return False
def blockexception(board):
    if(board[0]=='X' and board[8]=='X'and board[2]==' '):
        board[2] = "O"
        Draw_mark.draw(2,"O",board)
        return True
    elif(board[6]=='X' and board[2]=='X'and board[3]==' '):
        board[3] = "O"
        Draw_mark.draw(3,"O",board)
        return True
'''
//    elif(board[2]=='X' and (board[2][1]=='X' || board[3]=='X')  )
//
//      if(board[2][1]==' ')
//
//        board[2][1]='O'
//        return True
//
//      elif(board[3]==' ')
//
//        Draw_mark(3,"O")
//        return True
//
//
//
//    elif(board[6]=='X' and (board[2][1]=='X' || board[3]=='X')  )
//
//      if(board[2][1]==' ')
//
//        board[2][1]='O'
//        return True
//
//      elif(board[3]==' ')
//
//        Draw_mark(3,"O")
//        return True
//
//
//
'''



