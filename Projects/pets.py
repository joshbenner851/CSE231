
##
## Class PetError -- complete
##

class PetError( ValueError ):
    
    pass

##
## Class Pet -- not complete
##

class Pet( object ):
    
    def __init__( self, species=None, name="" ):
        species = species.lower()
        if species:
            species.lower()
            self.name_str = name.title()
            if(species=="dog" or species=="hamster" or species=="cat" or species=="horse" or species=="gerbil" or species=="ferret"):
                self.species = species
                self.name = name
            else:
                self.species = None
                self.name = ""
                raise PetError()
        else:
            self.species = None
            self.name = ""
            print(__str__(self))
            raise PetError()
        
    def __str__( self ):
        if(self.name):
            result_str = "Species of: " + self.species.title() + ", named " + self.name.title()

        else:
            result_str = "Species of: " + self.species.title() + ", unnamed"
        return result_str

##
## Class Dog -- not complete
##

class Dog( Pet ):

    def __init__(self,name="",chases="Cats"):
        Pet.__init__(self,"Dog")
        self.chases = chases
        self.name = name
    def __str__( self ):
        if(self.name):
            result_str = "Species of: " + self.species.title() + ", named " +\
            self.name.title() + ", chases " + self.chases

        else:
            result_str = "Species of: " + self.species.title() + ", unnamed " +\
            ", chases " + self.chases
        return result_str
##
## Class Cat -- not complete
##

class Cat( Pet ):
    
    def __init__(self,name="",hates="Cats"):
        Pet.__init__(self,"Cat")
        self.hates = hates
        self.name = name
    def __str__( self ):
        if(self.name):
            result_str = "Species of: " + self.species.title() + ", named " +\
            self.name.title() + ", hates " + self.hates

        else:
            result_str = "Species of: " + self.species.title() + ", unnamed " +\
            ", hates " + self.hates
        return result_str

