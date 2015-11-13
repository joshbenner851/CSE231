#! /usr/bin/python
 
Q=0
C=0
Aoz = 0
FABV = 0
IABV = 0
URange = 0
LRange = 0
Step = 0
 
Q = int(input("Please enter the final quantity of liquid you would like to achieve"))
C = int(input("Please enter the amount of caffeine you would like in the final product"))
IABV = float(input("Please enter the initial ABV of the alcohol you wish to use in decimal form"))
 
LRange = float(input("Please enter the minimum ABV you would like to attain in decimal form: "))
URange = float(input("Please enter the maximum ABV you would like to attain in decimal form:"))
 
Step = int(input("Please enter the decimal step in ounces that you would like to see your results in"))
 
while Aoz <= Q:
    FABV = (IABV*Aoz)/Q
    if FABV >= LRange and FABV <= URange:
        print (Aoz,"oz of",IABV*200," proof alcohol yields an ABV of",FABV*100,"leaving",Q-Aoz,"oz available for flavor in a",Q,"oz homebrew. In order to reach your desired caffeine quantity of",C,"mg, you will need an energy drink with a mg/oz of at least",C/Q)
    Aoz = Aoz + Step
