while(str!="exit"):
    str = input("Enter a command")
    if(str in "squares"):
        start = int(input("Enter the intial integer number in the series"))
        size = int(input("Enter the number of terms in the series"))
        Sum=0
        print("Sum = ",end="")
        for x in range(start,start+size):
            Sum += start*start
            start+=1
        print(Sum)
    elif(str in "cubes"):
        start = int(input("Enter the intial integer number in the series"))
        size = int(input("Enter the number of terms in the series"))
        Sum=0
        print("Sum = ",end="")
        for x in range(start,start+size+1):
            Sum += start*start*start
            start+=1
        print(Sum)
        #1+8+27
    elif(str in "exit"):
        print("Program halted normally")

    else:
        print("*** Invalid choice ***")
        str = "exit"
        
        
