#calculates GDP data for presidents
#uses txt and csv to extract and use data
#can't figure out how to return and set multiple items with a function
import csv
def open_extract():
    #opens files
    file_obj = open("the_correct_presidents.txt","r")
    gline1 = open("GDP_Section1All_Hist1.csv","r")
    gline2 = open("GDP_Section1All_Hist2.csv","r")
    count = 0
    #extracts data and sets years and gdp to a list
    for line in gline1:
        if(count==7):
            years = line
        elif(count==8):
            gdp = line
        count+=1
    #gets rid of extra stuff in list
    years = years[7:-51]
    #print(years)
    #print(gdp)
    count=0
    #extracts data for file 2
    for line in gline2:
        if(count==7):
            years1 = line
        elif(count==8):
            gdp1 = line
        count+=1
    #print(gdp1)
    #gets rid of extra stuff in list and rids of commas
    years1 = years1[11:-138]
    years = years + years1
    years = years.split(',')
    gdp = gdp[37:-50]
    gdp1 = gdp1[41:-138]
    gdp = gdp + gdp1
    gdp = gdp.split(',')
    years = years[19:]
    gdp = gdp[19:]
    #print("length is",len(years))
    #print("gdp l " , len(gdp))
    combined = []
    #combines years and gdp data
    for x in range(0,len(years)):
        a = [years[x],gdp[x]]
        combined.append(a)
        #print(years[x],gdp[x])
    #print(combined)
    pres = []
    count = 0
    name = []
    #goes through presidents file and breaks lines into a list of
    #name,term,party
    for line in file_obj:
        #ignores first line
        if(count>0):
            a = line.split(',')
            #print(a)
            #removes "Jr."
            if(count==7):
                a.remove(a[1])
            name=str(a[0])
           # print("a",name)
            name = name.split("+")
           # print('b',name)
           #strips names down to last name, and numbers into single indexes
            if(len(name)>1):
                name = str(name).split()
                name = name[2]+ "-" + name[-1]
            name = str(name).split()
            name = name[-1]
            name = name.strip("']")
            term = a[1].strip()
            term = term.split('-')
            party = a[2].strip()
            party = party[0]
            #print("a is ", party)
            #not actually a tuple, changed to a list
            pres_tuple = [name,term,party]
            #pres is becoming a list of all names,terms,party
            pres.append(pres_tuple)
        count+=1
    num_pres = len(pres)
    rep_tot = 0
    dem_years = 0
    rep_years = 0
    dem_tot = 0
    processed_data = []
    count=0
    #loops for # of presidents
    for x in range(0,len(pres)):
        gdp_chg=0
        gdp_tot = 0
        gdp_tot2 = 0
        #finds term year start/finish
        start_year = int(pres[x][1][0])
        end_year = int(pres[x][1][1])
        length = end_year-start_year
        #print("start", start_year , " end: " , end_year)
        for y in range(0,length):
            #calculates GDP if one or two terms
            if(length<5):
                gdp_chg = combined[count+y][1].strip("'")
                gdp_chg = float(gdp_chg)
                #print(gdp_chg)
                gdp_tot += gdp_chg
                #print("the total change was ", gdp_tot)
            elif(length>4):
                for y in range(0,4):
                    gdp_chg = combined[count+y][1].strip("'")
                    gdp_chg = float(gdp_chg)
                   # print(gdp_chg)
                    gdp_tot += gdp_chg
                   # print("the total change was ", gdp_tot)
                #print("first term over")
                gdp_chg=0
                gdp_tot2 = 0
                count+=4
                #second term calculations
                for y in range(0,4):
                    gdp_chg = combined[count+y][1].strip("'")
                    gdp_chg = float(gdp_chg)
                    #print(gdp_chg)
                    gdp_tot2 += gdp_chg
                    #print("the total change was ", gdp_tot2)
                break
        if(length<5):
            if(pres[x][2][0]=="R"):
                rep_tot+=gdp_tot
                rep_years +=length
            elif(pres[x][2][0]=="D"):
                dem_tot+=gdp_tot
                dem_years+=length
            gdp_tot /=4
            #print("gdp was" ,gdp_tot)
            pres[x].append(round(gdp_tot,1))
        if(length>4):
            if(pres[x][2][0]=="R"):
                rep_tot+=gdp_tot + gdp_tot2
                rep_years +=length
            elif(pres[x][2][0]=="D"):
                dem_tot+=gdp_tot+gdp_tot2
                dem_years+=length
            
            gdp_tot /=4
            pres[x].append(round(gdp_tot,1))
           # print("gdp1 was", gdp_tot)
            gdp_tot2/=4
            pres[x].append(round(gdp_tot2,1))
            #print("gdp2 was", gdp_tot2)
        #print("gdp was " ,gdp_tot/4)
        count+=4
        
   # print(pres)
    dem = round(dem_tot/dem_years,1)
    rep = round(rep_tot/rep_years,1)
    
    count = 0
    #crazy formatting crap
    print("GDP Growth by Presidential Term")
    print()
    print()
    for x in range(0,num_pres):
        if(len(pres[x])>4 and count<2):
            form="{:} {:5} {:1} {:1} {:1} {:1}"
            print(form.format(pres[x][0] ,"1", "(",pres[x][3],"):",pres[x][2]*int(round(pres[x][3],0))))
            print(form.format(pres[x][0],"2", "(",pres[x][4],"):",pres[x][2]*int(round(pres[x][4],0))))
        elif count==1:
            a = 5
        elif(count>6 and count<8):
            form="{:} {:9} {:1} {:1} {:1} {:1}"
            print(form.format(pres[x][0] ,"1", "(",pres[x][3],"):",pres[x][2]*int(round(pres[x][3],0))))
            print(form.format(pres[x][0],"2", "(",pres[x][4],"):",pres[x][2]*int(round(pres[x][4],0)))) 
        elif(len(pres[x])>4 and count>8 and count<10):
            form="{:} {:8} {:1} {:1} {:1} {:1}"
            print(form.format(pres[x][0] ,"1", "(",pres[x][3],"):",pres[x][2]*int(round(pres[x][3],0))))
            print(form.format(pres[x][0],"2", "(",pres[x][4],"):",pres[x][2]*int(round(pres[x][4],0)))) 
        elif(len(pres[x])>4 and count>8 and count<11):
            form="{:} {:11} {:1} {:1} {:1} {:1}"
            print(form.format(pres[x][0] ,"1", "(",pres[x][3],"):",pres[x][2]*int(round(pres[x][3],0))))
            print(form.format(pres[x][0],"2", "(",pres[x][4],"):",pres[x][2]*int(round(pres[x][4],0)))) 
        else:
            form="{:16} {:1} {:1} {:1} {:1}"
            print(form.format(pres[x][0], "(",pres[x][3],"):",pres[x][2]*int(round(pres[x][3]))))
        count+=1
    print()
    form="{:16} {:1} {:1} {:1} {:1}"
    print(form.format("Democrat", "(",dem,"):", "D"*int(round(dem,0))))
    print(form.format("Republican","(",rep,"):","R"*int(round(rep,0))))
    #for x in range(0,lens(pres)):
    #    print(form.format(pres[x][0])
    file_obj.close()
    gline1.close()
    gline2.close()
    
      
        

    



def main():  
    open_extract()



    
main()
