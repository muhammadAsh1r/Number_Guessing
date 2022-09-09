from random import randint


def game():
    random_number = randint(0, 10)
    chances = 3
    while chances > 0:
        guess = int(input('Guess a number: '))

        if guess == random_number:
            print('Congratulations! you guessed it successfully.')
            break
        else:
            chances -= 1
            print('Try Again!')

        if chances == 2:
            if random_number > 5:
                hint = "The number is greater than 5"
                print(hint)
            else:
                hint = 'The number is less than 5'
                print(hint)
        if chances == 1:
            if random_number % 2 == 0:
                hint = "The number is divisible by 2"
                print(hint)
            elif random_number % 3 == 0:
                hint = "The number is divisible by 3"
                print(hint)
            else:
                hint = 'The number is not divisible 2 and 3'
                print(hint)
    else:
        print('Better luck next time.')
        restart = input('Type Y to play again or N to quit:').upper()
        if restart == 'Y':
            game()
        else:
            print('See ya!')


game()
