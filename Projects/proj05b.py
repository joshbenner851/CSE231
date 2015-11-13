#ask for file to open
#write to file given by user
#prompt for a region code and give report that calculates
# num of, total pop, avg pop, smallest and largest pop

#gets name of file to open
def open_file():
    input_str = input("Enter a input file")
    return input_str
#opens and processes file
def process_file(input_str):

    try:
        file_obj = open(input_str,"r")
        year = input("Please enter a year 1990-2012")
        year = year.lower()
        if(year != "quit"):
            region= input("Please enter a 3 digit region code")
            #defaults until list is searched for highest/lowest/avg pop etc
            count = 0
            total_pop = 0
            lowest_pop = 999999999999999
            highest_pop = 0
            avg_pop = 0
            pop = 0
            lowest_name = ""
            highest_name = ""
            for line in file_obj:
                line = line.strip()
                #compares region
                region_set = line[56:59]
                if(region == region_set):
                    pop = line[-10:].strip()
                    #scans all of file
                    if(year == "" or year == "all" or year == "ALL"):
                        count+=1
                        pop = int(pop)
                        total_pop += pop
                        #finds highest/lowest pop
                        if(pop>highest_pop):
                            highest_pop = pop
                            highest_name = line[5:50].strip()
                        if(lowest_pop>pop):
                            lowest_pop=pop
                            lowest_name = line[5:50].strip()
                    line = line.strip()
                    year_set = line[:len(year)]
                    #scans only for that year
                    if (year == year_set):
                        count+=1
                        pop = int(pop)
                        total_pop += pop
                        if(pop>highest_pop):
                            highest_pop = pop
                            highest_name = line[5:50].strip()
                        if(lowest_pop>pop):
                            lowest_pop=pop
                            lowest_name = line[5:50].strip()
            avg_pop = (total_pop/count)*1000
            avg_pop = round(avg_pop,0)
            avg_pop = int(avg_pop)
            #printing for region
            if(region == "AFR"):
                print("Report for Africa in ",year)
            elif(region == "AMR"):
                print("Report for Americas in ",year)
            elif(region == "SEAR"):
                print("Report for South-East Asia in ",year)
            elif(region == "EUR"):
                print("Report for Europe in ",year)
            elif(region == "EMR"):
                print("Report for Eastern Mediterranean in ",year)
            elif(region == "WPR"):
                print("Report for Western Pacific in ",year)
            #formats all totals
            total_pop = '{:,}'.format(total_pop*1000)
            higest_pop = '{:,}'.format(highest_pop*1000)
            lowest_pop = '{:,}'.format(lowest_pop*1000)
            avg_pop = '{:,}'.format(avg_pop)
            print("The total count is " , count)
            print("The total pop is ", total_pop)
            print("The average pop is ",avg_pop)
            print("The highest pop is", highest_name, "with a population of", highest_pop)
            print("The lowest pop is", lowest_name, "with a population of",lowest_pop)
            return file_obj
            
        #quit was entered in year
        else:
            print("Program has been halted")
            file_obj.close()
    #error handling
    except FileNotFoundError:
        print("The file was not found")
        input_str = open_file()
        process_file(input_str)
#calls open/process
def main():
    input_str = open_file()
    process_file(input_str)
    

#does stuff, see previously
main()
