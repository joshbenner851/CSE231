def open_file():
    input_str = input("Enter a input file")
    return input_str
#opens and processes file
def process_file(input_str):
    try:
        file_obj = open(input_str,"r")
        count = 0
        values = []
        benford = [30.1,17.6,12.5,9.7,7.9,6.7,5.8,4.1,4.6]
        for a in range(0,9):
            values.append(0)
        for line in file_obj:
            line = line.strip()
            a = int(line[0])
            count+=1
            #print(a)
            values[a-1]+=1
        print("Digit Percent Benford")
        form="{:5} {:1} {:5} {:1} {:3} {:1}"
        for y in range(1,9):
            percent = "{:2f}".format((values[y]/count)*100)
            print(form.format(y, ": ",round(float(percent),1) , "%  (",benford[y-1], "%)"))
    except FileNotFoundError:
        print("The file was not found")
        input_str = open_file()
        process_file(input_str)
def main():
    input_str = open_file()
    process_file(input_str)
    

#does stuff, see previously
main()

    
        
