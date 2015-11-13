
import string
from operator import itemgetter


def add_word( word_map, word ):

    #checks to make sure it's a word, not empty string
    if word:
        #if word is not in the dictionary, add it to dict
        if word not in word_map:
            word_map[ word ] = 0

        #if reoccurence, add to count
        word_map[ word ] += 1


def build_map( in_file, word_map ):

    for line in in_file:

        #makes list of every word in file
        word_list = line.split()

        for word in word_list:

            #strip all punctuation and send to add function
            word = word.strip().strip(string.punctuation)
            word = word.lower()
            add_word( word_map, word )
        

def display_map( word_map ):

    word_list = list()

    #make list of everything in dictionary
    for word, count in word_map.items():
        word_list.append( (word, count) )

    #sort list by frequency
    alpha_list=sorted(word_list,key=itemgetter (0))
    freq_list = sorted( alpha_list, key=itemgetter(1),reverse=True )
    
    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format(item[0],item[1]) )
    #needs work
        '''
    for word,count in word_list:
        print( "{:15s}{:5d}".format( word,count ) )
    '''
def open_file():

    try:
        input_str = input("Please enter a input file")
        in_file = open( input_str, "r" )
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file


def main():

    word_map = dict()
    in_file = open_file()

    if in_file != None:

        build_map( in_file, word_map )
        display_map( word_map )
        in_file.close()


main()
