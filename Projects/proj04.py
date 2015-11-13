print("Tuition Calculator")
print()
str1 = "yes"
while(str1!="no"):
    fees = 3.00
    tuition =0
    res = input("Resident (Yes/No):")
    grade = input("Input level- freshman, sophomore, junior, senior, graduate: ")
    cred = int(input("Input credits this semester: "))
   # print(cred)
    res = res.lower()
    grade = grade.lower()
    college = ""
    fees = 3.00
    tuition =0
    if(cred>5):
        fees+=5.00
    if(grade!="graduate"):
        fees+=18.00
    else:
        fees+=9.25
    if(grade!="freshman"):
        college = input("College - business, engineering, health, science, none:")
        college = college.lower()
    if(res == "yes"):
        if(grade == "freshman" or grade == "sophomore"):
            tuition += cred*440.00
        elif(grade == "junior" or grade ==  "senior"):
            tuition += cred*490.25
            if(cred<4):
                if(college == "business"):
                    fees+=100.00
                elif(college == "engineering"):
                    fees+=361.00
                elif(college == "health" or college == "sciences"):
                    fees+=50.00
            else:
                if(college == "business"):
                    fees+=200.00
                elif(college == "engineering"):
                    fees+=590.00
                elif(college == "health" or college == "sciences"):
                    fees+=100.00
        elif(grade == "graduate"):
            tuition += cred*646.00
            fees+=37.50
            if(cred<5):
                fees+=37.50
            else:
                fees+=75.00
    elif(res == "no"):
        if(grade == "freshman" or grade == "sophomore"):
            tuition += cred*1165.50
        elif(grade == "junior" or grade == "senior"):
            tuition += cred*1202.25
            if(cred<4):
                if(college == "business"):
                    fees+=100.00
                elif(college == "engineering"):
                    fees+=361.00
                elif(college == "health" or college == "sciences"):
                    fees+=50.00
            else:
                if(college == "business"):
                    fees+=200.00
                elif(college == "engineering"):
                    fees+=590.00
                elif(college == "health" or college == "sciences"):
                    fees+=100.00
        elif(grade == "graduate"):
            if(college == "engineering"):
                if(cred<5):
                    fees+=361.00
                    fees+=37.50
                else:
                    fees+=590.00
                    fees+=75.00
            tuition += cred*1269.00
    
    print("Total bill: $", '{:,.2f}'.format(tuition+fees))
    print()
    str1 = input("Do you want to calculate again (Yes/No):")
    str1 = str1.lower()
    

