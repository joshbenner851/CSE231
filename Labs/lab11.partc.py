
import string

def build_word_set( input_file ):
    
    word_set = set()
    
    for line in input_file:

        #stripping white space and build a list of word
        word_lst = line.strip().split()

        # changes all words to lowercase and strips the punctuation
        # for every word in the list
        word_lst = [w.lower().strip(string.punctuation) for w in word_lst]
        
        for word in word_lst:
            
            if word != "":

                # if it's not an empty string, ie a word, add to word set
                word_set.add( word )
                
    return word_set


def compare_files( file1, file2 ):
    #set of shared words
    setf1 = build_word_set(file1)
    setf2 = build_word_set(file2)
    unique1 =  setf1 & setf2
    #set of all words
    unique2 = setf1 | setf2
    print(len(unique2))
    print(unique1)
    # Build two sets:
    #   all of the unique words in file1
    #   all of the unique words in file2

    # Display the total number of unique words between the
    # two files.  If a word appears in both files, it should
    # only be counted once.

    # Display the number of unique words which appear in both
    # files.  A word should only be counted if it is present in
    # both files.

  
     
######################################################################

f1 = open( "document1.txt" )
f2 = open( "document2.txt" )

compare_files( f1, f2 )

f1.close()
f2.close()

