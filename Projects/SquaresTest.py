prompt= ""
def squares():
    print("running squares")
while(prompt!="exit"):
    prompt = (str)(input("Please enter a command"))
    if(prompt == "squares"):
        squares()
    elif(prompt == "cubes"):
        cubes()




