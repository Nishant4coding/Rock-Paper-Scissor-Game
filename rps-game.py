import random

print("~~~~~~~Welcome to Rock Paper Scissor~~~~~~~")

user_score=0
comp_score=0
ties=0

name=input("Enter your name here: ")
print("""
    Choices....
    1--> Rock
    2--> Paper
    3--> Scissor

    Winning Rules...
    1. Paper vs Rock --> Paper
    2. Rock vs Scissors --> Rock
    3. Scissor vs Paper --> Scissor""")
while True:
    choice=int(input("Enter your choise from 1-3: "))
    print()

    while choice>3 or choice <1:
        choice=int(input("Enter the valid Choice.."))


    if choice==1:
        user_choice="Rock"

    elif choice==2:
        user_choice="Paper"

    else:
        user_choice="Scissor"
    print()

    print("~~Now it's computer's turn~~")
    computer=random.randint(1,3)

    if computer==1:
        comp_choice="Rock"
    elif computer==2:
        comp_choice="Paper"
    else:
        comp_choice="Scissor"

    print("The computer choice is",comp_choice)
    print()

    if choice==computer:
        result="Draw"
        print("match draw")

    elif (choice==1 and computer==2) or (choice==3 and computer==1) or (choice==2 and computer==3):
        result=comp_choice
        print("Winner is computer")

    elif (choice==2 and computer==1) or (choice==1 and computer==3) or (choice==3 and computer==2):
        result=user_choice
        print("You Won the match")


    if result=="Draw":
        ties+=1

    elif result==comp_choice:
        comp_score+=1

    else:
        user_score+=1
    print()
    print ("~~~Score Board~~~")

    print(name,": ",user_score)
    print("Computer: ",comp_score)
    print("Draw: ",ties)
    print()

    replay=input("Are you want to play again? ")
    print()
    if replay=="no" or replay=="No" or replay=="NO" or replay=="N" or replay=="n":
        break

print("Game Over")
print("Thanks for Playing")