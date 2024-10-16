# random generate
# use se puchna hai
import random

no_to_be_guess = random.randint(1,100)

while True:
    try:
        user_guess =  int(input('Guess the Number between 1 to 100 '))
        if user_guess == no_to_be_guess:
            print(f'\n Congratulations!! {no_to_be_guess} is the Right Answer \n')
        elif user_guess > no_to_be_guess:
            print("It's too High")
        elif user_guess < no_to_be_guess:
            print("It's too Low")
    except ValueError:
        print('Invalid Input')


