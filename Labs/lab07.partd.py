prompt= ""
def get_integer( prompt ):
    value_str = input( prompt )
    try:
        value_int = int( value_str )
    except EOFError:
        print("** End of File, assumming none **")
        value_int = "none"
    return value_int

def cubes():
    start = get_integer( "Enter the starting term: " )
    terms = get_integer( "Enter the amount of terms: " )
    sum = 0
    for x in range(start,start+terms):
        sum += start**3
    print("Sum of cubes = ", sum)
def squares():  
    start = get_integer( "Enter the starting term: " )
    terms = get_integer( "Enter the amount of terms: " )
    sum = 0
    for x in range(start,start+terms):
        sum += x**2
    print("Sum of squares = ", sum)
while(prompt!="exit"):
    prompt = input("Please enter a command")
    if(prompt == "squares"):
        squares()
    elif(prompt == "cubes"):
        cubes()
    else:
        print("** Invalid Choice **")
