import random

cards=[1,2,3,4,5,6,7,8,9,10,10,10,10]

repeat=input("Do you want to play a game of blackjack? Type 'y' for yes and 'n' for 'no' ")
while repeat=="y":
    print('''
      _ _ _ _ ___ ___ _ _ _ ___ _ _ _________
 |A|Q|1|5|4  |7  |J|1|9|7  |A|K|2        |
 |@|@|@|@|@  |## |O|O|O|OO |+|+|+        |
 | | | | | @ |   | | | |   | | |    +    |
 | | | | |   | # | | | | O | | |         |
 | | | | | @ |   | | | |   | | |    +    |
 | | | | |   | # | | | | O | | |        +|
 | | | | |   |   | | | |   | | |        Z|
  ~ ~ ~ ~ ~~~ ~~~ ~ ~ ~ ~~~ ~ ~ ~~~~~~~~~
''')
    user=[]
    computer=[]
    a=random.choice(cards)
    user.append(a)
    b=random.choice(cards)
    user.append(b)
    print("Your cards are: "+ str(user))
    usersum=sum(user)
    x=random.choice(cards)
    y=random.choice(cards)
    computer.append(x)
    computer.append(y)
    print("Computer's first card is "+ str(computer[0]))
    computersum=sum(computer)
    choice=input("Type 'y' to get another card, type 'n' to pass: " )
    if choice=="y":
        c=random.choice(user)
        usersum+=c
        print(f"Your third card is {c}")
        if usersum>21:
            print("You lost")
            print("Your Score: "+ str(usersum))
            print("Computer's Score: "+ str(computersum))
        elif usersum>computersum:
            print("You Won! 🤩")
            print("Your Score: "+ str(usersum))
            print("Computer's Score: "+ str(computersum))
        elif usersum==computersum:
            print("Draw! 😶")
            print("Your Score: "+ str(usersum))
            print("Computer's Score: "+ str(computersum))
        
        else:
            print("Computer Won! You Lost! 🥺")
            print("Your Score: "+ str(usersum))
            print("Computer's Score: "+ str(computersum))


    else:
        if usersum>computersum:
            print("You Won 🤩!")
            print("Your Score: "+ str(usersum))
            print("Computer's Score: "+ str(computersum))
        elif usersum==computersum:
            print("Draw! 😶")
            print("Your Score: "+ str(usersum))
            print("Computer's Score: "+ str(computersum))
        
        else:
            print("Computer Won! You Lost! 🥺")
            print("Your Score: "+ str(usersum))
            print("Computer's Score: "+ str(computersum))
    repeat=input("Do you want to play again? ")
        

