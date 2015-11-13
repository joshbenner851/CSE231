

def main():
    file_name = input("Please enter your name + .txt like josh.txt")
    try:
        file_obj = open(file_name,"r")
        first_time()
    except FileNotFoundError:
        file_obj = open(file_name,"w")
        first_time()
def edit_file():
    '''nothing'''
def first_time():
    classes = int(input("How many classes do you have"))
    credit = int(input("How many credits are you taking"))
    for x in range(classes):
        class_name = input("Enter class name: ")
        num_categories = int(input("Enter number of categories for grades"))
        x=0
        for y in range(0,num_categories):
            x+=1
            '''change to make a list'''
            categories = input("For Category: Enter the Category name and percent of grade(Exam2 15)")
        #add which category you want to add grades to
        adding = input("Do you have any current grades to enter")
        if(adding == "yes"):
            grades_list = input("Enter each grade seperated by a space")
            grades = grades_list.split(" ")
            print(grades)
        
main()
