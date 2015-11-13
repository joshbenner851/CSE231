
class Amount(object):
    
    def __init__( self, val=0, code="USD" ):
        '''initializes a Amount object with self,value, and code as params
        ,default values are assigned if no params sent in'''
        #checking for valid type of value
        if(type(val) is int or type(val) is float):
            self.__value = val
            #checking for valid of type for code
            if(type(code) is str):
                #checking if code is vaid: USD,SEK,CHF,GBP
                if(code=="USD" or code=="SEK" or code=="CHF" or\
                  code=="GBP"):
                    self.__code = code
                #invalid code message and make Amount with defaults
                else:
                    print("Invalid code of dollar, only USD,SEK,CHF, and GBP accepted.\
Default object was returned")
                    self.__value = 0
                    self.__code ="USD"
            #invalid type message for code and make Amount with defaults
            else:
                print("Code must be a string")
                self.__value = 0
                self.__code ="USD"
        #invalid type message for value and make Amount with defaults
        else:
                print("Invalid type for value. Default object was returned")
                self.__value = 0
                self.__code ="USD"
    def __str__( self ): #always returns a string
        '''returns a string of value and code, value rounded 2decimals'''
        if(self is Amount):
            str1 = "{:.02f}".format(self.__value)
            return str(str1)+","+ self.__code
        else:
            print("Item sent in was not an Amount Obj"
            

    def __repr__( self ):
        '''returns a string of value and code, value isn't rounded'''
        return str(self.__value) + " " + self.__code

    def convert( self, code="USD" ):
        
        amount = 0
        gbp = .638244
        sek = 7.38837
        chf = .959220
        try:
            if(code=="GBP"):
                if(self.__code=="USD"):
                    amount = self.__value*gbp
                elif(self.__code=="SEK"):
                    amount = (self.__value/sek)*gbp
                elif(self.__code=="CHF"):
                    amount = (self.__value/chf)*gbp
                elif(self.__code=="GBP"):
                    amount = self.__value
            elif(code=="SEK"):
                if(self.__code=="USD"):
                    amount = self.__value*sek
                elif(self.__code=="SEK"):
                    amount = self.__value
                elif(self.__code=="CHF"):
                    amount = (self.__value/chf)*sek
                elif(self.__code=="GBP"):
                    amount = (self.__value/gbp)*sek
            elif(code=="USD"):
                if(self.__code=="USD"):
                    amount = self.__value
                elif(self.__code=="SEK"):
                    amount = (self.__value/sek)
                elif(self.__code=="CHF"):
                    amount = (self.__value/chf)
                elif(self.__code=="GBP"):
                    amount = self.__value/gbp
            elif(code=="CHF"):
                if(self.__code=="USD"):
                    amount = self.__value*chf
                elif(self.__code=="SEK"):
                    amount = (self.__value/sek)*chf
                elif(self.__code=="CHF"):
                    amount = self.__value
                elif(self.__code=="GBP"):
                    amount = (self.__value/gbp)*chf
            return Amount(amount,code)
        except Exception as e:
            print("Error was " , e, ". Default object was returned.")
            return Amount()
    def __eq__( self, other ):
            boolean = False
            temp = other.convert(self.__code)
            if(self.__value==temp.__value):
                boolean = True
            else:
                boolean = False
            return boolean

    def __ne__( self, other ):
            boolean = False
            temp = other.convert(self.__code)
            if(self.__value!=temp.__value):
                boolean = True
            else:
                boolean = False
            return boolean

    def __lt__( self, other ):
            boolean = False
            temp = other.convert(self.__code)
            if(self.__value<temp.__value):
                boolean = True
            else:
                boolean = False
            return boolean

    def __le__( self, other ):
            boolean = False
            temp = other.convert(self.__code)
            if(self.__value<=temp.__value):
                boolean = True
            else:
                boolean = False
            return boolean

    def __add__( self, other ):
        amount = 0
        if(type(other) is int or type(other) is float):
            amount  = self.__value + other
        elif(type(other) is Amount):
            amount = self.__value + other.convert(self.__code).__value
        else:
            print("Other was not a int,float, or valid amount.")
            print("Returned default Amount")
        return Amount(amount,self.__code)

    def __radd__( self, other ):
        amount = 0
        if(type(other) is int or type(other) is float):
            amount  = self.__value + other
        else:
            amount = self.convert(other.__code)+other
        return Amount(amount,self.__code)

    def __sub__( self, other ):
        amount = 0
        if(type(other) is int or type(other) is float):
            amount  = self.__value - other
        else:
            amount = other.convert(self.__code).__value-self.__value
        return Amount(amount,self.__code)

    def __rsub__( self, other ):
        amount = 0
        if(type(other) is int or type(other) is float):
            amount  = other - self.__value
        else:
            amount = other - self.convert(other.__code)
        return Amount(amount,self.__code)

