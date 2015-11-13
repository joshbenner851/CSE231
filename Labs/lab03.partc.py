
num=1
evens = 0
odds = 0
sumEven = 0
sumOdd = 0
posNums = 0
while num!=0:
    text = input("Input an integer (0 terminates)")
    num = int(text)
    
    if num>=0:
        if num%2==0:
            evens+=1
            sumEven+=num
        else:
            odds+=1
            sumOdd+=num
        posNums+=1
    else:
        print(num, " is a negative integer")

print("sum of odds ", sumOdd)
print("sum of evens ", sumEven)
print("odd count ", odds)
print("even count ",evens)
print("total positive int count ", posNums)

        
             
