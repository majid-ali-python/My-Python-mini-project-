# Ya Mara Python Ka Mini Project Hai JO k Expense Tracker Hai
# Ma nay isy loops, conditional , list , dictionary  say banay hai or basic inut ka b user kia hai 
Expense = []


while (True):
    print("Welcome to Majid Ali Mini Poject of Expense Tracker")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Amount of Expenses")
    print("4. Exit")
   
    selection = int(input("Plese select the number"))
    # If user Enter button 1 then this process is done
    if selection==1:
        date = input("On which day did you spend")
        item = input("On what item did you spend? (like fruit,cloths,mobile etc)")
        amount = int(input("How much did you spend?(Enter amount)"))

    # now i can save it in dictionary and append the dictionary to Expense list
        selection_dic = {
        "date" : date,
        "item" : item,
        "amount": amount
        }
        Expense.append(selection_dic)
        print("Congratulation your data is save ")
    # If user Enter 2 then this process is done
    if selection==2:
        if (len(Expense)==0):
            print("Expense is not added.")
        else:
            print("This is Your All Expenses")
            count = 1
            for allvalue in Expense:
                print(f"Expense Number{count}={allvalue["date"]},{allvalue["item"]},{allvalue["amount"]}")
                count +=1
    # If user Enter 3 then this process is done
    if selection==3:
        print("This is You Total Expene:")
        sum =0
        for allvalue in Expense:
            sum= sum+allvalue["amount"]
        print(sum)
    # If user Enter the 4 then program is closed 
    if selection==4:
        print("This Software is Exit\nThaks TO Visit Majid Ali Expense Tracke  ")
        break
           
        
