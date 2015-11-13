
file_name = input("Enter a file name")
input_file = open( file_name, "r" )

for line in input_file:
    line = line.rstrip()
    print( line )

input_file.close()
