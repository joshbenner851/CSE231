#copy selected lines from population.txt
#write to file given by user



Done = False
while not Done:
    try:
        file_obj = open('population.txt')
        outfile_str = input("Enter a file to write to")
        outfile_obj = open(outfile_str,'w')
        year = input("Please enter a year")
        Done = True
        for line in file_obj:
            line = line.strip()
            if(year == "" or year == "all" or year == "ALL"):
                print(line,file=outfile_obj)
            year_set = line[:len(year)]
            if (year == year_set):
                print(line,file=outfile_obj)
        outfile_obj.close()
        file_obj.close()
    except FileNotFoundError:
        print("Program halted")         # executed on file open error
       


