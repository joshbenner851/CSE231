import math
length = input("Enter the length of one side(ft)")
Length = float(length)

spacing = input("What's the recommended spacing between plants(in)")
Spacing = float(spacing)

depthBed = input("Enter the depth of the flowerbeds(ft)")
DepthBed = float(depthBed)

depthFill = input("Enter the depth of the fill areas(ft)")
DepthFill = float(depthFill)
radius = Length/4
Flower_Circle_area = math.pi * radius*radius
Fill_Area = ((Length*Length) - 3*Flower_Circle_area)/9 
plantNums = Flower_Circle_area  / ((Spacing*Spacing)/144)
plantNums = int(plantNums)

SoilArea = DepthBed*Flower_Circle_area/27
FillArea = (DepthFill*Fill_Area)/3

print("Summary of your plant needs:")
print("Each outer semi-circular bed: ",plantNums//2," plants")
print("The center circular bed ",plantNums," plants")
print("Total: " ,plantNums+ 4*(plantNums//2), " plants")
print()
print("Summary of your soil needs:")
print("Each outer semi-circular bed: ",round((SoilArea/2),1) ," cubic yards")
print("The center circular bed ",round((SoilArea),1) ," cubic yards")
print("Total: " ,round((round((SoilArea/2),1)*4 + round(SoilArea,1)),1) , " cubic yards")
print()
print("Summary of your fill needs: ")
print("Total: " ,round(FillArea,1) , " cubic yards")
