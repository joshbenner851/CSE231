count = int(input("Input the order of a Latin square"))

if count<1 or count>9:
    print()
    print("*** Invalid order of square ***")
    print("*** (must be between 1 and 9) ***")
    print()
    print("Program halted")
else:
    start = int(input("Input the top-left number"))
    if start<1 or start>count:
        print()
        print("*** Invalid value for top-left number ***")
        print("*** (must be between 1 and" , count, ") ***")
        print()
        print("Program halted")
    else :
        print()
        for x in range(0,count+1):
            if start<=count:
                for x in range(0,count+1):
                    if start<=count :
                        print(start,end=" ") 
                        start+=1
                    else:
                        start=1
                start+=1
                print()
            else:
               start=1

