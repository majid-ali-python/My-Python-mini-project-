# This is expense tracker mini project in python using (loops, conditionals,list,dictionary and input/output)

# ma list expese  ki  bana raha dictionary ki form ma  hou jis ma user jo b kharcha wagar kary ga 
expenses = []
print("Welcome to expense tracker :")

while True:
    print("=====MENUE=====") 
    print("1. Add expense")        
    print("2. View all expenses")
    print("3. View total amount")
    print("4. Exit")

    choice = int(input("Enter your choice"))
    # add expenxe
    if(choice==1):
        date = input("Kis din kharcha kia th ap nay ?")
        catagory = input("Kis type/catagory ka kharcha kia tha ap nay ?(like food, cloth, buy mobile etc koi b kharcha kia ho ap nay)")
        description = input("Aur batao kia kharcha kia th ya description do")
        amount = int(input("Total kitna kharcha th ap ka ?"))

        # ab ma expense ki dectionay banata hou 
        expense={
            "date" : date,
            "catagory" : catagory,
            "description" : description,
            "amount" : amount
        }
        expenses.append(expense)
        print("Done Bro, App ka expense successfully add ho gya hai !")

# ab 2 wala point VIEW ALL EXPENSES
    if(choice==2):
        if(len(expenses)==0):
            print("App ka koi kharcha ni hai beta ? jao pehly kharcha karo ")
        else:
            print("Ye hai ap ka sara kharcha")
            count = 1
            for eachkharcha in expenses:
                print(f"kharcha Number{count}->{eachkharcha["date"]}, {eachkharcha["catagory"]}, {eachkharcha["description"]}, {eachkharcha["amount"]}")
                count = count + 1
# ab agar user 3 buttuon ko enter kary (VIEW TOTAL EXPENSE)
    elif(choice==3):
        total = 0
        for eachkharcha in expenses:
            total = total + eachkharcha["amount"]
        print("\nTotal kharcha is =", total)

# ab agar user 4 button ko enter karta hai to EXIT 
    elif(choice==4):
        print("Shukria ap nay Majid Ali k system ko use kia ! be happy ")
        break
   
