from datetime import date
import random
import soundfile
import sounddevice
import play_song




# play_song.play_game_song()
name = str(input('Enter your name: '))



def start_game():

    play = 'Lets play guess the number to start guess a number between 1 and 10: ' + name
    rules = 'Guess the number you get 3 attempts good luck'
    level1 = 'level 1 pick betweeen 1 and 3'
    print(play)
    print(rules)
    print(level1)
    secret = random.randint(1, 4)
    auto_win = int(1234)
    limited_attempts = int(0)
    while True:
        try:
            guess = int(input('enter a number: '))
            if guess == secret:
                print('correct')
                print('You win: ' + name)
                break
            elif guess == auto_win:
                print('You win: ' + name)
                quit()
            else:
                limited_attempts += 1
                print(f'Incorrect try again you have: {3 - limited_attempts} left')
                if limited_attempts == 3:
                    print('game over')
                    break
        except ValueError:
            print('Please enter a number')
    play_again()


def play_again():
    again = input('would you like to play again ? (y/n): ').lower()

    try:
        
        if again == 'y':
            return start_game()
        elif again == 'm':
            print('something new')
            sounddevice.stop()
        else:
            print('game over')
            sounddevice.stop()

    except ValueError:
        print('please enter (y/n): ')

start_game()
