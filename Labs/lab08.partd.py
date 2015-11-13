#form="{:20} {:8} {:8} {:8}"
#form.format()
def open_file():
        input_str = input("Please enter a input file")
        return input_str
def process_file(input_str):
    try:
        file_obj = open(input_str)
        name = ""
        exams = ()
        #line = 4th alpha
        #4th tuple added to my list
        info = []
        for line in file_obj:
            name = line[:20].strip()
            exams = line[20:]
            exams  = exams.split()
            exam1 = int(exams[0])
            exam2 = int(exams[1])
            exam_avg = (exam1+exam2) / 2
            #print("the avg was " ,exam_avg)
            info += [name,exam1,exam2,exam_avg]
        return info
    except IOError:
        print("File opening failed")         # executed on file open error
        input_str = input("Try again to enter a file to open:")
        process_file(input_str)
def main():
    stuff = []
    input_str = open_file()
    process_file(input_str)
    stuff += process_file(input_str)
    print(stuff)
    count = 0
    for y in range(2):
        for x in range(16):
            if(stuff[x]>stuff[x+4]):
                temp = stuff[x:x+4]
                stuff[x:x+4] = stuff[x+4:x+8]
                stuff[x+4:x+8] = temp
                x+=4
    '''    
    name_len = []
    length = []
    for x in range(0,20):
        if(x%4==0 and x!=0):
            string = stuff[x]
            name_len = len(string)
            x+=4
    for x in range(5):
        length = 20 - name_len[x]
    
    for x in range(20):
        
            print()
            print(stuff[x])
            
        else:
            print(stuff[x])
    '''
    
    print("Name                       Exam1   Exam2   ExamAvg")
    for y in range(16):
        if(y%4==0):
            #print(stuff[y], " "*name_len[y], "   " , stuff[y+1], "   ", stuff[y+2], "   ", stuff[y+3])
            #print(stuff[y] ,"{.20d}".format(stuff[y+1]), "{.20d}".format(stuff[y+2]),"{.20d}".format(stuff[y+3]))
            #print(stuff[y], "{:20d}".format(stuff[y+1]))
            print("{:20}".format(stuff[y]) , "{:8d}".format(stuff[y+1]),"{:7d}".format(stuff[y+2]),"{:9.1f}".format(stuff[y+3]))
            y+=4
    
main()
    
