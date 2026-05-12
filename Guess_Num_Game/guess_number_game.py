from datetime import date
import random
import soundfile
import sounddevice
import play_song




play_song.play_game_song()
name = str(input('Enter your name: '))

def play_level(level_name, min_num, max_num):
    print(level_name)

    secret_number = random.randint(min_num, max_num)
    limited_attempts = 3
    auto_win = 1234

    while limited_attempts > 0:
        try:
            guess = int(input(f'Enter a number between {min_num} and {max_num}: '))

            if guess == secret_number:
                print('correct')
                return True
            
            elif guess == auto_win:
                print('You win: ' + name)
                return False

            else:
                limited_attempts -= 1

                if limited_attempts > 0:
                    print(f'Incorrect you have: {limited_attempts} attempts left')

                else:
                    print('game over')
                    print(f'The correct number was: {secret_number}')
                    return False
                
        except ValueError:
            print('Please enter a number')

def start_game():
    print(f'Lets play Guess The Number, {name}!')
    print('You get 3 attemps per level.')

    level_1 = play_level('LEVEL 1 (1-3)', 1, 3)

    if level_1:
        level_2 = play_level('LEVEL 2 (1-6)', 1, 6)

        if level_2:
            level_3 = play_level('LEVEL 3 (1-10)', 1, 10)

            if level_3:
                level_legendary = play_level('LEVEL LEGENDARY (1-20)', 1, 20)

                if level_legendary:
                    print(f'Congratulations {name}, you beat the game!')
   

def play_again():
    while True:
        again = input('would you like to play again ? (y/n): ').lower()

        if again == 'y':
            start_game()
        
        elif again == 'n':
            print('Thank you for playing!')
            sounddevice.stop()
            break
        else:
            print('please enter (y/n): ')

start_game()
play_again()
