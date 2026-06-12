import random
#0 for Rock
#1 for Paper
#2 for Scissors
user = int(input("Enter your choice : (0 = rock, 1 = paper, 2 = scissors)"))
computer = random.randint(0,2)
if user >= 3 or user < 0:
    print("You entered the invalid number. You lose")
else :
    print(f"Computer choice : {computer}")

    if user == computer:
        print("It's Draw")
    elif user == 2 and computer == 0:
        print("You lose")
    elif user == 0 and computer == 2:
        print("You win")
    elif user < computer:   #0 < 2
        print("You lose")
    elif user > computer:   #2 > 0
        print("You win")
