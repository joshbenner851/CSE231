import turtle
turtle.down()
board = ["","","","","","","","",""]
class Tic_tac_toe(object):
    def __init__(self,):
        print("Tic Tac Toe")
        self.board = ["","","","","","","","",""]
        self.drawn = False
    def draw(self):
        '''draws the playing grid and the ‘X’s and ‘O’s
        that have been played '''
        
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
            drawn = True

    def set_mark(self,mark,index):
        '''checks board of (1-9) for a X or O to see if
        a mark has been placed there. 1 = not taken, 0 = taken '''
        spot = index
        if(board[index-1]!=""):
            return 0
        else:
            board[spot] = mark
            Draw_mark.draw(index,mark,self.board)
            return 1
    def determine_winner(self):
        '''returns X if player wins, O if computer wins, or None for no-one'''
        #default, returns None if no one wins=unchanged through logic
        winner = None
        #checks horizontal win for player/computer
        for x in range(0,7):
            if(board[x]==board[x+1] and board[x+1]==board[x+2] and board[x]=="X"):
                winner = "X"
                break
            elif(board[x]==board[x+1] and board[x+1]==board[x+2] and board[x]=="O"):
                winner =  "O"
                break
            x+=3
        #checks vertical win for player/computer
        for x in range(0,3):
            if(board[x]==board[x+3] and board[x+3]==board[x+5] and board[x]=="X"):
                winner ="X"
                break
            elif(board[x]==board[x+3] and board[x+3]==board[x+5] and board[x]=="O"):
                winner = "O"
                break
        #checks if computer has middle spot, checks player diag win
        if not board[4]=="O":
            #diagonal check
            if board[0]=="X" and board[4]=="X" and board[9]=="X":
                winner = "X"
            #other diag check
            elif board[2]=="X" and board[4]=="X" and board[6]=="X":
                winner = "X"
        #check computer diag win
        else:
            if board[0]=="O" and board[4]=="O" and board[9]=="O":
                winner = "O"
            elif board[2]=="O" and board[4]=="O" and board[6]=="O":
                winner = "O"
        return winner

    def full_board(self):
        '''returns True if all 9 slots are full otherwise returns False '''
        full = False
        count = 0
        for x in range(0,9):
            if(board[x]!=""):
                count+=1
        if(full==9):
            full = True
        return full
class Draw_mark(object):
    def __init__():
        print()
    def draw(spot,mark,board):
        turtle.up()
        turtle.back(10)
        if(spot==1 or spot==4 or spot==7):
            if(spot==4):
                turtle.right(90)
                turtle.forward(100)
                turtle.left(90)
                turtle.down()
                if(mark=="X"):
                    drawX()
                else:
                    drawO()
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
        elif(spot==2 or spot==5 or spot==8):
            turtle.forward(100)
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


def drawX():
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
    turtle.up()
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.down()
    turtle.circle(40)
    turtle.up()
    
def computer_play(game):
    board = game.board
    c = False
    b = False
    if(   board[4]==' '):
        Draw_mark.draw(index,"O",board)
        c= True
    if(c==True):
        print('aaaa')
    else:
        
        #loop for win takes horiz/vertical
        for y in range(0,2):
            if(b==True):
                break
            for x in range(0,3):
                #horizontal win take checks
                if(board[0+x]=="O" and board[1+x]=="O" and board[2+x]==' '):
                    board[2+x] = 'O'
                    b = True
                    break
                elif(board[0+x]=="O" and board[1+x]=='' and board[2+x]=="O"):
                    board[1+x] = 'O'
                    b = True
                    break
                elif(board[0+x]=="" and board[1+x]=='O' and board[2+x]=='O'):
                    board[0+x] = 'O'
                    b = True
                    break
                #vertical win take checks
                if (board[0+x+y]=="O" and board[1+x+y]=="O" and board[2+x+y]==""):
                    board[2+x+y] = 'O'
                    b = True
                    break
                elif (board[1+x+y]=="O" and board[2][a]=='O'and board[0][a]==''):
                    board[1+x+y] = 'O'
                    b = True
                    break
                elif (board[0+x+y]=="O" and board[2][a]=='O' and board[1][a]==''):
                    board[0+x+y] = 'O'
                    b = True
                    break
                x+=3
            y+=2
    #diagonals
    if(b==True):
        print("asfa")
    elif (board[0]=='O' and    board[4]=='O' and board[8]==' '):
            Draw_mark(8,"O")
             
    elif (board[8]=='O' and    board[4]=='O' and board[0]==' '):
            Draw_mark(0,"O")
             
    elif(board[0]=='O' and board[8]=='O' and    board[4]==' '):
            Draw_mark.draw(4,"O")
             
    elif (board[6]=='O' and    board[4]=='O' and board[2]==' '):
            Draw_mark(2,"O")
             
    elif (board[2]=='O' and    board[4]=='O' and board[6]==' '):
            Draw_mark(6,"O")
             
    elif (board[2]=='O' and board[6]=='O' and    board[4]==' '):
            Draw_mark.draw(4,"O")
             
     
    a = False
  #loops for loss horiz/vert block
    for y in range(0,2):
        if(a==True):
            break
        for x in range(0,3):
            #horizontal win block
            print("XXX")
            if (board[0+x]=='X' and board[1+x]=='X' and board[2+x]==''):
                    Draw_mark(2+x,"O")
                    break
                    a = True
            elif (board[0+x+y]=='X' and board[1+x+y]=='' and board[2+x+y]=="X"):
                    Draw_mark(1+x,"O")
                    break
                    a = True
            elif (board[0+x+y]=='' and board[1+x+y]=='X' and board[2+x+y]=='X'):
                    Draw_mark(0+x,"O")
                    break
                    a = True
            #vertical win block
            if (board[0+x+y]=='X' and board[1+x+y]=='X'and board[2+x+y]=="X"):
                    board[2+x+y] = 'O'
                    break
                    a = True
            elif (board[0+x+y]=='X' and board[1+x+y]=='X'and board[2+x+y]==' '):
                    board[1+x+y] = 'O'
                    break
                    a = True
            elif (board[0+x+y]=='X' and board[1+x+y]=='X' and board[2+x+y]==' '):
                    board[0+x+y] = 'O'
                    break
                    a = True
    if(a==True):
        print("ended computer turn")
    #block win diagonals
    elif (board[0]=='X' and    board[4]=='X' and board[8]==' '):
        Draw_mark.draw(8,"O")
     
    elif (board[8]=='X' and    board[4]=='X' and board[0]==' '):
        Draw_mark.draw(0,"O")
     
    elif(board[0]=='X' and board[8]=='X' and    board[4]==' '):
        Draw_mark.draw(4,"O")
     
    elif (board[6]=='X' and    board[4]=='X' and board[2]==' '):
        Draw_mark.draw(2,"O")
     
    elif (board[2]=='X' and    board[4]=='X' and board[6]==' '):
        Draw_mark.draw(6,"O")
     
    elif (board[2]=='X' and board[6]=='X' and    board[4]==' '):
        Draw_mark.draw(4,"O")  
    elif(board[0]==' '):
        Draw_mark.draw(0,"O")
         
    elif (board[2]==' '):
        Draw_mark.draw(2,"O")
         
    elif (board[6]==' '):
        Draw_mark.draw(6,"O")
         
    elif(board[8]==' '):
        Draw_mark.draw(8,"O")
         
    elif(board[0]=='X' and board[8]=='X'and board[2]==' '):
        Draw_mark.draw(3,"O")
         
    elif(board[6]=='X' and board[2]=='X'and board[3]==' '):
        Draw_mark.draw(3,"O")
         
