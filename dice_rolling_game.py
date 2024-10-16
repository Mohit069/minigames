import random

while True:
    val = input('Roll the dice? (y/n): ').lower()
    if val == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1} , {die2})')
    elif val == 'n':
        print('Thanks!')
        break
    else:
        print('Invalid Input')
