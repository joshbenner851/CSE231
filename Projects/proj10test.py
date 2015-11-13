import money
#initializing
print("Initializing")
A = money.Amount(9.59220,"CHF")
B = money.Amount(10.0,"USD")
print(A==B)
print()
print("Wrong initializations")
C = money.Amount("X","CHF") #invalid value, should give warning message
C = money.Amount(2.00,"LBP") #invalid code, should give warning
print()
print("Ending initializing")
print()
print("Testing str and repr methods")
#testing str and repr methods, str= rounded val to 2 decimals
print(str(A))
#should give all digits in val
print(repr(A))
print("Str and repr have been run")
print()
D = money.Amount(6.77,"USD")
E = money.Amount(50,"SEK")
print("D is ", D)
print("E is ", E)

print("Conversion E to USD: ",E.convert("USD"))
print(D==E.convert("USD"))
print(E==D.convert("SEK"))
print("Converting D to SEK: ",D.convert("SEK"))
print("Converting to D not acceptable code, CAN: ",D.convert("CAN"))
print("Converting E to a not acceptable code, 123: ",E.convert(123))
print()
E = money.Amount(55,"SEK")
print("Reinitializing E to new value: ", E)

# testing __add__
print("Numerator Tests:")
print("Addition Test: " ,D+5)
#testing object addition
print("Object Addition Test of USD+SEK,: " ,D+E)
print("Object Addition Test of SEK+USD,: " ,E+D)
print("Wrong other type: ", D+'xx')
# testing __radd__
print("Radd addition Test: " ,5+D)
#testing __sub__
print("Subtraction Test: ", E-2)
#testing object subtraction
print("Object Subtraction Test of USD-SEK: ",D-E)
print("Object Subtraction Test of SEK-A: ",E-D)
#testing __rsub__
print("Rsub: " ,100-E)
print("End numerator tests")
print()
print("Testing eq,ne,lt,le")
#testing 
print("Equivalency Test of A and B ",A==B)
print("Not Equal Test of A and E " ,A!=E)
print("Less than Test of A and D " ,A<D)
print("Less than or equals Test of A and B ",A<=B)



