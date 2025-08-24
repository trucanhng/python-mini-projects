import random

print("============================================")
print("========= Rock-Paper-Scissors Game =========")
print("============================================")
print("Game Rules:")
print("-- Rock crushes scissors.")
print("-- Scissors cuts paper.")
print("-- Paper covers rock.")
print("============================================")

choices = ["rock", "paper", "scissors"]

while True:
    # User choice
    user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
    while user_choice not in choices:
        user_choice = input("Please choose rock, paper, or scissors: ").strip().lower()

    # Computer choice
    computer_choice = random.choice(choices)

    print(f"You chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")
    print(f"\n{user_choice.capitalize()}  vs.  {computer_choice.capitalize()}\n") 

    # Determine the winner
    if user_choice == computer_choice:
        print("🤝🤝🤝 It's a tie! 🤝🤝🤝")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("🎉🎉🎉 You win! 🎉🎉🎉")
    else:
        print("😝😝😝 You lose! 😝😝😝")
    
    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again.startswith('n'):
        print("✋ Bye bye. See you next time!")
        break


