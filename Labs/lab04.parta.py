
AAA = "A"
BBB = "B"
CCC = 1
DDD = 11
EEE = 13
FFF = 5
GGG = 4.5
HHH = 1.8e-40

A = "A" <= BBB <= "Z"
print( "Value of A:", A )            # Value of A: ____________

B = GGG < HHH or EEE < FFF
print( "Value of B:", B )            # Value of B: ____________

C = not AAA >= BBB
print( "Value of C:", C )            # Value of C: ____________

D = not AAA < BBB or HHH > 0.0
print( "Value of D:", D )            # Value of D: ____________

E = DDD >= GGG or GGG >= 10
print( "Value of E:", E )            # Value of E: ____________

PPP = 4*DDD < 3*EEE
QQQ = (FFF+3)*2 >= 2*EEE-5
RRR = FFF + 3 > DDD
F = PPP or QQQ and RRR
print( "Value of F:", F )            # Value of F: ____________

G = DDD == 10 or 11
print( "Value of G:", G )            # Value of G: ____________
