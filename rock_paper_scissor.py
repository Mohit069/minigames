import random

emojis = {'r': ' Rock 💎','p':'Paper 📃','s':'Scissor ✂️'}
choices = ['r','p','s']

while True:
    user_choice = input("Choose one Among Rock, Paper, Scissor (R,P,S): ").lower()

    if user_choice not in choices:
        print("Invalid Output")
        continue

    computer_choice = random.choice(choices)

    print(f'You chose - {emojis[user_choice]}')
    print(f'Computer chose - {emojis[computer_choice]} ')

    if user_choice == computer_choice:
        print("Tie!!")
    elif(
            (user_choice == 'r' and computer_choice== 's')
         or (user_choice == 'p' and computer_choice == 'r')
         or (user_choice == 's' and computer_choice == 'p')):
        print("You win")

    else:
        print("You Lose!!")

    again_continue = input("want to play again? (y/n) ").lower()

    if again_continue == 'n':
        print("Bye!! We Had a Great Time ")
        break
