
##
## Demonstrate some of the operations of the Pet classes
##

import pets

def main():
    
    try:

        # Hamster
        A = pets.Pet( "Hamster" )
        print("A is a " , A)
        A = pets.Cat("Dora the Explorer","mice")
        print("A reinitialized and is now " ,str(A))
        print( A )       
        # Dog named Fido who chases Cats
        B = pets.Dog( "Fido" )
        print( B )

        # Cat named Fluffy who hates everything
        C = pets.Cat( "Fluffy", "everything" )
        print(str(C))
        print( C )
        B = pets.Pet("penguin")

    except pets.PetError:
        
        print( "Got a pet error." )

main()

