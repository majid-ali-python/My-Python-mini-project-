#Ya hai student management system using python procedual language

print("==========Welcome to Majid Ali Student Management System========= ")
print("1. Add Student")
print("2. View all Student")
print("3. Search Student")
print("4. Update Student")
print("5. Delete Student")
print("6. Calculate Average")
print("7. Exit")

Student = []
while (True):
    choice = int(input("Enter the number"))
    if(choice==1):
        Name = input("Enter name of Student ")
        Roll_num = int(input("Enter Your Roll Number"))
        Age = int(input("Enter Age of Student"))
        Department= input("Enter Department Name")
        Marks = int(input("Enter Your Marks"))

        std_dic ={
            "Name" : Name,
            "Roll_Num": Roll_num,
            "Age": Age,
            "Department": Department,
            "Marks": Marks
        }
        Student.append(std_dic)
        print("Congratulation Your Data is Store Successfully")

    if(choice==2):
        if (len(Student)==0):
            print("Your Data is Emply . ")
            print("Fill Your Data")
        else:
            for i in Student:
                print("This is Your All Data",i)
    if(choice==3):
        rollnumber = int(input("Enter Student Roll_Number do you want to Search"))
        found = False
        for i in Student:
            if rollnumber==i["Roll_Num"]:
                print(i)
                found= True
                break
        if not found:
            print("Invalid Rollnumber")
                        
    if (choice==4):
        rollnumber = int(input("Enter Student Roll_Number do you want to Update"))
        found = False
        for i in Student:
            if (rollnumber==i["Roll_Num"]):
                New_Marks = int(input("Enter new marks of the student"))
                i.update({"Marks":New_Marks})
                print(i)
                found =True
                break
        if not found:
            print("Invalid RollNumber")

    if (choice==5):
        rollnumber = int(input("Enter Student Roll_Number do you want to Delete"))
        found = False
        for i in Student:
            if (rollnumber==i["Roll_Num"]):
                Student.remove(i)
                print(i)
                found= True
                break
        if not found:
            print("Invalid RollNumber")
    if (choice==6):
        if(len(Student)==0):
            print("Student Data is Empty")
            print("Enter Student Data")
        else:
            total_marks= 0
            for i in Student:
                total_marks = total_marks +i["Marks"]
            average = total_marks / len(Student)
            print(average)
    if (choice==7):
        print("Exit")
        break
