str2 = "aababaa"
s3 = "abcdef"
print(s3[2:])
s3 = s3[::-1]
print(s3)
newstr = "" 
print (str2[::-1])
for x in range(len(str2)):
    if(str2[x] =="a"):
        a =5
    else:
        newstr +=str2[x:]
        break
print(newstr)
               
