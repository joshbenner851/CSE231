word = ""
while(word!="quit"):
    word = input("Enter a word to be translated to pig latin")
    word.lower()
    arr = []
    if(word.find('a')>-1):
        arr.append(word.find('a'))
    if(word.find('e')>-1):
        arr.append(word.find('e'))
    if(word.find('i')>-1):
        arr.append(word.find('i'))
    if(word.find('o')>-1):
        arr.append(word.find('o'))
    if(word.find('u')>-1):
        arr.append(word.find('u'))
    print(min(arr))
    if(word[0] == "a" or word[0] == "e" or word[0] == "i" or
       word[0] == "o" or word[0] == "u"):
        print(word + "way")
    else:
        print(word[min(arr):] + word[0:min(arr)] + "ay")
   # for x in word:  # enumerate() works well here
   #     if x in "aeiou":
   #         a==x
   #         break
   # print(word[a])

              
    
    
