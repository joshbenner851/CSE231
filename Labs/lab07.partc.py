
def get_integer( prompt ):
    value_str = input( prompt )
    try:
        value_int = int( value_str )
    except EOFError:
        print("** End of File, assumming none **")
        value_int = "none"
    except ValueError:
        print ( "** Invalid input, assuming 0 **" )
        value_int = 0
    
    return value_int

def main():
    try:
        while(get_integer != "none"):
            
            numer = get_integer( "Enter the numerator: " )
            denom = get_integer( "Enter the denominator: " )
            print( numer, "divided by", denom, end=" " )
            result = numer/denom
            print( "yields", result )

    except ZeroDivisionError:
        print( "** Invalid: attempted to divide by zero **" )
    except EOFError:
        print("** End of File, assumming none **")
    print( "Program halted" )

main()
