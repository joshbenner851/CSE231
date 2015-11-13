#ask for file to open
#write to file given by user
#prompt for a region code and give report that calculates
# num of, total pop, avg pop, smallest and largest pop

def open_file():
    input_str = input("Enter a input file")
    return input_str
def process_file(input_str):
    try:
        file_obj = open(input_str,"r")
        year = input("Please enter a year")
        year = year.lower()
        if(year != "quit"):
            region= input("Please enter a 3 digit region code")
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
                region_set = line[56:59]
                if(region == region_set):
                    pop = line[-10:].strip()
                    if(year == "" or year == "all" or year == "ALL"):
                        count+=1
                        pop = int(pop)
                        total_pop += pop
                        if(pop>highest_pop):
                            highest_pop = pop
                            highest_name = line[5:50].strip()
                        if(lowest_pop>pop):
                            lowest_pop=pop
                            lowest_name = line[5:50].strip()
                    line = line.strip()
                    year_set = line[:len(year)]
                    if (year == year_set):
                        count+=1
                        pop = int(pop)
                        total_pop += pop
                        if(pop>highest_pop):
                            highest_pop = pop
                            higest_name = line[5:50].strip()
                        if(lowest_pop>pop):
                            lowest_pop=pop
                            lowest_name = line[5:50].strip()
                avg_pop = (total_pop/count)*1000
                avg_pop = round(avg_pop,0)
                avg_pop = int(avg_pop
                '''
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
                '''
                total_pop = '{:,}'.format(total_pop*1000)
                higest_pop = '{:,}'.format(highest_pop*1000)
                lowest_pop = '{:,}'.format(lowest_pop*1000)
                avg_pop = '{:,}'.format(avg_pop)
                print("The total count is " , count)
                print("The total pop is ", total_pop)
                print("The average pop is ",avg_pop)
                print("The highest pop is", highest_name, " with a population of", highest_pop)
                print("The lowest pop is", lowest_name, " with a population of",lowest_pop)
                return file_obj
        else:
            print("Program has been halted")
    except FileNotFoundError:
        print("The file was not found")
        input_str = open_file()
        process_file(input_str)
        
def main():
    input_str = open_file()
    process_file(input_str)

    
main()
