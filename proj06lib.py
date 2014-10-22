import turtle
#draws horizontal rectangle

def draw_flag(name,width,orientation):
    #
    name = name.lower()
    orientation = orientation.lower()
    #checks to make sure width is >0, else asks for new width
    while(width<=0):
        width = int(input("Please enter an appropiate"\
        "width that is greater than 0"))
    currentpos2 = turtle.pos()
    #print(currentpos2 , "current pos is")
    #distinguishes what country should be drawn
    if(name=="norway"):
        #calculates the length from proportions
        length = width * 1.375
        #finds orientation
        if(orientation=="landscape"):
            #calls the big rectangle
            draw_horizrect(length,width,"red")
           # print("the length is " , length, " and the width is ", width)
            turtle.right(90)
            #goes down the left edge to start position for cross
            turtle.forward(width*.375)
            turtle.left(90)
            #draws the cross
            draw_cross(length,width,"red","thick")
        #if portrait, turtle is rotated 90degreees
        #everything else stays the same
        elif(orientation=="portrait"):
            turtle.right(90)
            draw_horizrect(length,width,"red")
           # print("the length is " , length, " and the width is ", width)
            turtle.right(90)
            turtle.forward(width*.375)
            turtle.left(90)
            draw_cross(length,width,"red","thick")
    #1. more countries but proportions, and colors change
    elif(name=="iceland"):
        length = width * 1.3888
        if(orientation=="landscape"):
            draw_horizrect(length,width,"blue")
           # print("the length is " , length, " and the width is ", width)
            turtle.right(90)
            turtle.forward(width*.375)
            turtle.left(90)
            draw_cross(length,width,"blue","thick")
        elif(orientation=="portrait"):
            turtle.right(90)
            draw_horizrect(length,width,"blue")
           # print("the length is " , length, " and the width is ", width)
            turtle.right(90)
            turtle.forward(width*.375)
            turtle.left(90)
            draw_cross(length,width,"blue","thick")
    #same as 1.
    elif(name=="faroe islands"):
        length = width * 1.375
        if(orientation=="landscape"):
            draw_horizrect(length,width,"white")
            #print("the length is " , length, " and the width is ", width)
            turtle.right(90)
            turtle.forward(width*.375)
            turtle.left(90)
            draw_cross(length,width,"white","thick")
        elif(orientation=="portrait"):
            turtle.right(90)
            draw_horizrect(length,width,"white")
           # print("the length is " , length, " and the width is ", width)
            turtle.right(90)
            turtle.forward(width*.375)
            turtle.left(90)
            draw_cross(length,width,"white","thick")
    #2.more countries but besides color and proportion change,
    #distance down flag to start cross changes
    elif(name=="denmark"):
        length = width * 1.32
        if(orientation=="landscape"):
            draw_horizrect(length,width,"crimson")
           # print("the length is " , length, " and the width is ", width)
            turtle.right(90)
            turtle.forward(width*(12/28))
            turtle.left(90)
            draw_cross(length,width,"crimson","thin")
        elif(orientation=="portrait"):
            turtle.right(90)
            draw_horizrect(length,width,"crimson")
            #print("the length is " , length, " and the width is ", width)
            turtle.right(90)
            turtle.forward(width*(12/28))
            turtle.left(90)
            draw_cross(length,width,"crimson","thin")
    #same as 2.
    elif(name=="sweden"):
        length = width * 1.6
        if(orientation=="landscape"):
            draw_horizrect(length,width,"navy")
           # print("the length is " , length, " and the width is ", width)
            turtle.right(90)
            turtle.forward(width*(12/28))
            turtle.left(90)
            draw_cross(length,width,"navy","thin")
        elif(orientation=="portrait"):
            turtle.right(90)
            draw_horizrect(length,width,"navy")
            #print("the length is " , length, " and the width is ", width)
            turtle.right(90)
            turtle.forward(width*(12/28))
            turtle.left(90)
            draw_cross(length,width,"navy","thin")
    #same as 2.
    elif(name=="finland"):
        length = width * 1.6363
        if(orientation=="landscape"):
            draw_horizrect(length,width,"ghost white")
            #print("the length is " , length, " and the width is ", width)
            turtle.right(90)
            turtle.forward(width*(12/28))
            turtle.left(90)
            draw_cross(length,width,"ghost white","thin")
        elif(orientation=="portrait"):
            turtle.right(90)
            draw_horizrect(length,width,"ghost white")
            #print("the length is " , length, " and the width is ", width)
            turtle.right(90)
            turtle.forward(width*(12/28))
            turtle.left(90)
            draw_cross(length,width,"ghost white","thin")
    #country wasn't typed properly
    else:
        print("This input is invalid")
    turtle.penup()
    turtle.setpos(currentpos2)
    turtle.setheading(0)
    #print("set position to", currentpos2)
#draws a horizontal box that is used for
#the big flag but also a smaller rectangle for the cross
def draw_horizrect(length,width,color):
    turtle.color(color)
    turtle.begin_fill()
    #loops to draw the width and length sides
    for x in range(4):
        #draws length
        if(x%2==0):
            turtle.forward(length)
        #draws width
        else:
            turtle.forward(width)
        turtle.right(90)
    turtle.end_fill()
    
#draws a horizontal and vertical rectangle
#to make a cross
def draw_cross(length,width,color,style):
    #precaution
    style.lower()
    #uses the base color to determine the 1st cross color
    if(color=="red" or color =="blue"):
        color2 = "white"
    elif(color=="white"):
        color2 = "dodger blue"
    elif(color=="crimson"):
        color2="snow"
    elif(color=="ghost white"):
        color2 = "blue"
    elif(color=="navy"):
        color2 = "yellow"
    #gets position to use later
    currentpos = turtle.pos()
    #uses color to determine type of flag prop to use
    if(color=="crimson" or color=="navy" or color=="ghost white"):
        #uses flags proportions to determine the small side for
        #the crosses rectangles
        w2 = width*.1428
        #calls a horizontal rectangle
        draw_horizrect(length,w2,color2)
        #moves distance forward to draw a vertical rectangle
        turtle.forward(length*(12/37))
        turtle.left(90)
        #print("the length is " , length, " and the width is ", width)
        #draws vertical rectangle
        draw_vertrect(width,w2,color2)
    #changes width because second cross
    else:
        w2 = width*.25
        draw_horizrect(length,w2,color2)
        turtle.forward(length*(6/22))
        turtle.left(90)
        #print("the length is " , length, " and the width is ", width)
        draw_vertrect(width,w2,color2)
    #distuingishes if a second cross needs to be drawn
    if(style=="thick"):
        #uses colors to determine the 2nd cross color
        if(color=="red"):
            color = "blue"
        elif(color=="blue"):
            color = "red"
        elif(color=="white"):
            color = "light coral"
        #turtle.speed(1)
        #repositioning for second cross
        turtle.penup()
        turtle.setpos(currentpos)
        turtle.pendown()
        turtle.right(90)
        #finds distance to move down and start point for 2nd cross
        turtle.forward(width*.0625)
        turtle.left(90)
        #calculating small side of crosses rectangles
        w2 *=.5
        draw_horizrect(length,w2,color)
        #new prop to move to set position for vert rectangle
        turtle.forward(length*(7/22))
        turtle.left(90)
        #print("the length is " , length, " and the width is ", width)
        draw_vertrect(width,w2,color)
        #print("the width of the second cross is" , width)
        
#draws the vertical rectangle of cross
def draw_vertrect(length,width,color):
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    #uses color to determine length of cross
    if(color=="blue" or color == "red" or color == "light coral"
       /or color=="yellow"):
        length*=.4375
    elif(color == "snow"or color=="navy" ):
        length*=.42857
    else:
        length*=.375
   # print("the length of the first " , length, " and the width is ", width)
    #loops to draw vertical rectangle
    for x in range(5):
        if(x%5==0):
            #draws first half of left vertical line
            turtle.forward((length))
           # print("drawing length")
        #draws from top of vertical to bottom of flag
        elif(x%2==0):
            turtle.forward(length*2+width)
            #print("drawing long side")
        #draws small side of vertical rectangle
        elif(x!=5):
            turtle.forward(width)
        turtle.right(90)
    turtle.end_fill()
#draw_flag("denmark",200,"PoRtrAit")
