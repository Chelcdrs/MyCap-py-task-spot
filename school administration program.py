import csv

def write_info_csv(info):
    with open('stud_info.csv', 'a', newline='') as csv_file:
        writer=csv.writer(csv_file)
        
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact","e-mail"])
            
        writer.writerow(info)
        
if __name__=='__main__':
    condition=True
    stud_num=1
    
    while(condition):
        stud_info=input("Enter student information for student #{} in the following format (Name Age Contact e-mail): ".format(stud_num))
        
        stud_info_list=stud_info.split(' ')
        
        print("The entered information is:\nName: {}\nAge: {}\nContact: {}\ne-mail: {}".format(stud_info_list[0], stud_info_list[1], stud_info_list[2], stud_info_list[3]))
        
        check=input("Is the entered information correct? Enter (yes/no): ")
        
        if check=="yes":
            write_info_csv(stud_info_list)
            
            con_check=input("Do you want to add information for another student? Enter (yes/no): ")
            if con_check=="yes":
                codition=True
                stud_num+=stud_num
            elif con_check=="no":
                condition=False
        elif check=="no":
            print("Please re-enter the information")