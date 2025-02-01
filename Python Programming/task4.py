print("Welcome to stone paper scissors game")
while(True):
    for i in range(3):
        print("\n")
    print("Press 1 to start the game")
    print("Press 2 for instructions")
    print("Press 3 to exit")
    choice = int(input())
    if choice == 1:
        player_score = 0
        computer_score = 0
        while(True):
            for i in range(5):
                print("\n")
            print("Enter your choice ==> stone(1), paper(2) or scissor(3) :")
            user_choice = input().lower()
            import random
            choices = ["stone", "paper", "scissor"]
            computer_choice = random.choice(choices)
            print("Computer choice is: ", computer_choice)
            if (user_choice == "stone" or user_choice == '1') and computer_choice == "scissor":
                print("You won")
                player_score += 1
            elif (user_choice == "stone" or user_choice == '1') and computer_choice == "paper":
                print("Computer won")
                computer_score += 1
            elif (user_choice == "paper" or user_choice == '2')and computer_choice == "stone":
                print("You won")
                player_score += 1
            elif (user_choice == "paper" or user_choice == '2')and computer_choice == "scissor":
                print("Computer won")
                computer_score += 1
            elif (user_choice == "scissor" or user_choice == '3') and computer_choice == "paper":
                print("You won")
                player_score += 1
            elif (user_choice == "scissor" or user_choice == '3')and computer_choice == "stone":
                print("Computer won")
                computer_score += 1
            else:
                print("It's a tie")
            
            print("Current score: ")
            print(f"You:{player_score}\nComputer:{computer_score}")
            play_again = input("press enter to play again else press 'N' to exit :")
            if play_again.lower() == "n":
                break
            else:
                continue
        print("***********************************************")
        if player_score > computer_score:
            print("You won the game")
        elif player_score < computer_score:
            print("Computer won the game")
        else:
            print("It's a tie")
        print("***********************************************")
        
    elif choice == 2:
        print("Instructions:")
        print("1. You have to choose between stone, paper and scissor")
        print("2. Stone beats scissor, scissor beats paper and paper beats stone")
        print("3. You will get 1 point for winning, 0 for tie and -1 for losing")
        print("4. You can play as many times as you want")
        print("5. You can exit the game anytime")
        dummy = input("Press any key to go back to main menu")
    
    elif choice == 3:
        print("Exiting the game")
        break
    else:
        print("Invalid input")
        continue

print("Thank you for playing the game")
        
