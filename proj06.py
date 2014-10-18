import turtle
#draws horizontal rectangle

def draw_flag(name,width,orientation):
    turtle.speed(1)
    name.lower()
    orientation.lower()
    #checks to make sure width is >0, else asks for new width
    while(width<=0):
        width = int(input("Please enter an appropiate"\
        "width that is greater than 0"))
    currentpos = turtle.pos()
    if(name=="norway"):
        length = width * 1.375
        draw_horizrect(length,width,"blue")
        width/=3
        length/=3
        turtle.right(90)
        turtle.forward(width)
        turtle.left(90)
        draw_cross(length,width,"red","xxx")
        
        
    elif(name=="denmark"):
        length = width * 1.32
    elif(name=="sweden"):
        length = width * 1.6
    elif(name=="faroe islands"):
        length = width * 1.375
    elif(name=="iceland"):
        length = width * 1.3888
    elif(name=="finland"):
        length = width * 1.63
    else:
        print("This input is invalid")
 

    
def draw_horizrect(length,width,color):
    turtle.color(color)
    turtle.begin_fill()
    for x in range(4):
        if(x%2==0):
            turtle.forward(length)
        else:
            turtle.forward(width)
        turtle.right(90)
    turtle.end_fill()
#draws both rectangles = cross
    '''
def draw_cross(length,width,color,style):
    style.lower()
    draw_horizrect(length,width,color)
    turtle.forward((width-length)/2)
    turtle.left(90)
    draw_vertrect(length,width,color)
'''
#original
def draw_cross(length,width,color,style):
    style.lower()
    draw_horizrect(length,width,color)
    turtle.forward((length-width)/2)
    turtle.left(90)
    draw_vertrect(length,width,color)

    
#draws the vertical rectangle of cross
def draw_vertrect(length,width,color):
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for x in range(5):
        if(x%5==0):
            turtle.forward((length))
        elif(x%2==0):
            turtle.forward(length*2+width)
        elif(x!=5):
            turtle.forward(width)
        turtle.right(90)
    turtle.end_fill()
