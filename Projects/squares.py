num = 0
sq = 0
cub = 0
count = 0
while(1):
    count+=1
    sq = count*count
    cub = count*count*count
    print("sq1: " , sq," cub: ",cub, " # ", count)
    if(sq+1==cub or cub+1==sq or sq-1==cub or cub-1==sq):
        print("sq: " , sq," cub: ",cub)
        break
    if sq>5000:
        break
