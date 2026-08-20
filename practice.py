# sab say pehly ma list banou ga jis ma sara kharcha save ho ga 
expense = []
print("🙋‍♂️🙋‍♂️  Welcome to Majid Ali expense tracker  🙋‍♂️🙋‍♂️")

while True:
    print("👉👉👉Select the Number 👈👈👈")
    print("1. ➕ Add expense here⬅️")
    print("2. 👀 View all expense")
    print("2. 👀 View total amount")
    print("4. ❌ Exit")

    # yaha par ma condition lagaou ga k agar user 1 ko enter kary to kia hona chahiya
    choice = int(input("🔍 Enter your choice "))
    if(choice==1):
        date = input("💭 Kis din kharcha kia th ?")
        items = input("😱 Kis cheez par kharcha ki th ?")
        description = input("Is k ilava koi or ❓")
        amount = int(input("💰 Kitny passy lagy"))

        # ab ma expense ki dictionary banaou ga k list ma store karny k lia 
        exp_dict={
            "date":date,
            "items": items,
            "description": description,
            "amount": amount
        }
        expense.append(exp_dict)
        print("👌🏻Done yar ! ap ka sara kharcha add ho gya hai successfully 👍🏻")

        # agar user 2 enter kary to kia hona chahiya
    if(choice==2):
        if(len(expense)==0):
            print("➕ Ap ka koi kharcha ni hai .To add karo apna kharcha")
        else:
            print("⬇️ Ya hai ap ka sara expense")
            count= 1
            for allexpense in expense:
                print(f"Kharcha number {count}➡️{allexpense["date"]},{allexpense["items"]},{allexpense["description"]},{allexpense["amount"]}")
                count= count+1
                # ab agar user 3 dubay to kia hona chahiya 
    elif(choice==3):
        total = 0
        for allkharcha in expense:
            total = total + allkharcha["amount"]
        print("\n📲 Total Kharcha is=",total)
    elif(choice==4):
        print("😇Shukria ap nay Majid Ali k software ko use kia 😇")
        break
