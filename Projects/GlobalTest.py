x = 10
y = 20
print(y)
def test(x):
    global y
    #y= y+1
    z = y+1
    print(y)
    print(z)


test(x)
print(y)
