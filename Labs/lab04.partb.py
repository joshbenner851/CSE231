
H = 10
I = 5
if H % 3 == 0:
    H -= 1
else:
    H +=3
    if (H // 2 == 4) or (H % 2 == 0):
        H += 1
        I = H + 10 * 3 // 5
    I += 2

print( "Value of H:", H )            # Value of H: ____________

print( "Value of I:", I )            # Value of I: ____________

J = 0
K = 25
  
if not (J == 0):
    J -= 1
else:
    J += 1
    K //= K // 2

print( "Value of J:", J )            # Value of J: ____________

print( "Value of K:", K )            # Value of K: ____________

L = 20
if (L != 20) or (L % 10 == 0):
    L += 1
    if L % 2 == 0:
        L += 5
    else:
        L += 7
    L -= 2
    if L % 5 > 2:
        L -=4
    L += 3
L -= 8

print( "Value of L:", L )            # Value of L: ____________
