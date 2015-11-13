import csv
#use census data to build a dictionary that can be used by a user
#and also output the information of population,migration,births
#finds min/max population and outputs these state/counties/info
def build_dict(file_obj):
    '''accepts a file object, builds a dictionary of
    (state,county):(pop,birth,migrate), then return this dictionary'''
    file = file_obj
    count=0
    
    pop_dict = {}
    lower_case_dict = {}
    for line in file:
        if count>1:
            line_lst = []
            line_lst = line.split(",")
            
            lower_case_dict[(line_lst[5].lower(),line_lst[6].lower())] = \
            (int(line_lst[12]),int(line_lst[20]),line_lst[67])
            pop_dict[(line_lst[5],line_lst[6])] = \
            (int(line_lst[12]),int(line_lst[20]),line_lst[67])
            #print(pop_dict[(line_lst[5],line_lst[6])])
        count+=1
    return pop_dict,lower_case_dict
def reverse_dict(pop_dict):
    '''accepts a dictionary of (state,county):(pop,birth,migrate),
    and reverse it, then returns this reversed dictionary'''
    reverse_pop_dict = {v:k for k,v in pop_dict.items()}
    #print(reverse_pop_dict , "reverse dict")
    return reverse_pop_dict
def find_CP(reverse_pop_dict):
    '''accepts a dictionary that is (pop,birth,migrate):(state,county),
    then builds list and sorts the list low/high, calls print function
    highest/lowest'''
    pop_list = []
    for values in reverse_pop_dict.keys():
        pop_list.append([values,reverse_pop_dict[values]])
    #pop_list = list(reverse_pop_dict)
    pop_list.sort()
    print("County with largest population:")
    print_nicely(pop_list[len(pop_list)-1])
    print("County with smallest population:")
    print_nicely(pop_list[0])
def ask_user(pop_dict,lower_case_dict):
        state = ""
        county = ""
        while(state!="quit" or county!="quit" or state!="q" or county!="q"):
            try:
                state = input("Which state or q/quit to halt:")
                state.lower()
                if(state=="quit" or state=="q"):
                    print("Program halted")
                    break
                county = input("Which state or q/quit to halt:")
                county.lower()
                if(county=="quit" or county=="q"):
                    print("Program halted")
                    break
                #print(lower_case_dict[(state,county)], " is this")
                stuff = [lower_case_dict[(state,county)],(state[0].upper() + state[1:]\
                ,county[0].upper() + county[1:])]
                print_nicely(stuff)
            except:
                print("Please enter valid input")
                continue
def print_nicely(stuff_list):
    '''accepts a list in the format [(pop,biths,netmigr),(state,county)]
    and prints them nicely in order, no return'''
    print("State name = " , stuff_list[1][0])
    print("County name = " , stuff_list[1][1])
    print("PopEst name = " , stuff_list[0][0])
    print("Births name = " , stuff_list[0][1])
    print("NetMigr name = " , stuff_list[0][2])
    
def main():
        '''basic frame to make sure file can be opened and catches and prints
        any errors that occured, calls all functions, closes file'''
        file_obj = open("CO-EST2013-Alldata.csv.txt","r")
        pop_dict = build_dict(file_obj)
        pop = pop_dict[0]
        lower = pop_dict[1]
        reverse_pop = reverse_dict(pop)
        find_CP(reverse_pop)
        ask_user(pop,lower)
        file_obj.close()
        '''
        except FileNotFoundError:
            print("Program has been halted because file couldn't be opened")
        except Exception as e:
            print("Something went wrong...")
            print(e)
        '''
    
main()
