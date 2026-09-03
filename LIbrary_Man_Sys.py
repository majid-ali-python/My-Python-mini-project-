#This is python mini project of Library Management System
print("=====Welcome to Majid Ali Library Management System=====")
print("1. Add Book")
print("2. View All Books")
print("3. Search Book")
print("4. Issue Book")
print("5. Return Book")
print("6. Delete Book")
print("7. Exit")

Book = []

while (True):
    choice = int(input("Enter Your Number"))
    if (choice==1):
        Book_Name= input("Enter the Book Name")
        Book_ID = int(input("Enter the Bookd ID (Special Number of Book)"))
        Author = input("Enter the Author of the Book")
        Catagory = input("Enter the Catagory (Programming, Science, History) of Book")
        Status = "Available"

        Book_Dic ={
            "Book_Name": Book_Name,
            "Book_ID": Book_ID,
            "Author": Author,
            "Catagory":Catagory,
            "Status": Status
        }

        Book.append(Book_Dic)
        print("Congratulation Your Book is Stored Successfuly")
       #View ALl Books
    if (choice==2):  
        if (len(Book)==0):
            print("Your Data Is Empty ! Please Enter Your Data First")
        else:
            for i in Book:
                print("Your All Boooks are:",i)

      #Search Book
    if (choice==3):
        found= False
        Search_Book = input("Enter the Book Name Do You Want To Search")
        for i in Book:
            if(Search_Book==i["Book_Name"]):
                print("This is Your Book:",i)
                found = True
                break
        if not found:
            print("Invalid Book Name Please Enter Correct Name of Book")
          

    #issue book
    if (choice==4):
        found = False
        Search_Book = input("Enter the Book Name Do You Want To Issue")
        for i in Book:
            if Search_Book==i["Book_Name"]:
                if i["Status"]=="Available":
                    i["Status"]="Issued"
                    print("Book issued Successfully")
                    print(i)
                    found= True
                    break
                else:
                    print("Book is already issued")
                    found= True
                    break

        if not found:
            print("Invalid Name of Book ! Please Enter Correct Name")

        #return book
    if (choice==5):
        found = False
        Search_Book = input("Enter the Book Name Do You Want To Return")
        for i in Book:
            
            if(Search_Book==i["Book_Name"]):
                if i["Status"]=="Issued":
                    i["Status"]="Available"
                    print("Books is Returned Successfully")
                    print(i)
                    found= True
                    break
                else:
                    print("Bookd is Already Available ")
                    found= True
                    break

        if not found:
            print("Invalid Book Name ! Please Enter Correct Book Name")

        #Delete Book
    if (choice==6):
        found = False
        Search_Book = input("Enter the Book Name Do You Want To Delete")
        for i in Book:

            if (Search_Book==i["Book_Name"]):
                Book.remove(i)
                found = True
                break

        if not found:
            print("Invalid Book Name ! Please Try Again")

    if (choice==7):
        print("Thanks for using Majid Ali Library Management System")
        print("Good Bye")
        break
                    


    

