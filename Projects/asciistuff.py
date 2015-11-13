def is_alpha(str s):
    for x in range(len(s)):
        if(s[x].isalpha()==False):
            break
            return false
        else:
            return true
def is_digit(str s):
    #same thing but for numbers, run through whole length of string
    #I can't remember if my for loop is declared right
    for x in range(len(s)):
        if(s[x].isalnum()==False):
            break
            return false
        else:
            return true
    
def to_lower( str ):
    bool state = True
    for x in range(len(s)):
        if(s[x].isalpha()==False):
            state = False
            break
    if(state=True):
        return s.tolower()
    
def to_upper( str ):
    bool state = True
    for x in range(len(s)):
        if(s[x].isalpha()==False):
            state = False
            break
    if(state=True):
        return s.tolower()
    
def find_chr( str, str ):
    return s1.index(s2)
def find_str( str, str ):
    return s1.find(s2)
def replace_chr( str, str, str ):
    #basically concatenate the beginning + new char + rest of string
    #highly recommend using find_chr to find where you're replacing
def replace_str( str, str, str ):
    #same as above but with strings
def trim_chr( str, str ) :
    #use find_chr/find_str but also use the rfind to find the last index
    
def trim_all( str, str ):
