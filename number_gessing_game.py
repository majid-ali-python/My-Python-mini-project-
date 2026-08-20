import random

secret_number = random.randint(1, 100)

while True:
    guess_number = int(input("Guess the number"))
    if guess_number > secret_number:
        print("Your number is greater then the origional number")
    elif guess_number < secret_number:
        print("Your number is less then the origional number ")
    else:
        print("Congratulation this is the real number ")
        break