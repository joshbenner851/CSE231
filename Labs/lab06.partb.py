file_name = input("Enter a file name to output to")
outfile_obj = open( file_name, "w" )
line_str = " "
while(line_str[0]!="."):
    line_str = input()
    if(line_str[0]=="."):
        break
    outfile_obj.write(line_str)
    outfile_obj.write("/n")
outfile_obj.close()
