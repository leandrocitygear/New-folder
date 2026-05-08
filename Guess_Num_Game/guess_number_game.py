from datetime import date
import random
import soundfile
import sounddevice
import play_song

date = date.today()
formatted_date = date.strftime("%B %d, %Y")


player_ids = list(range(1, 100001))

player_id = random.choice(player_ids)

play_song.play_game_song()
name = str(input('Enter your name: '))
age = int(input('Enter your Age: '))
location = str(input('Where do you live: '))
welcome = 'Welcome to Guess the number Game ' + name 


print(f'''
Hello: {name} 
Age: {age} 
Location: {location} 
player ID: {player_id}
Account created on: {formatted_date}
{welcome}
''')

def start_game():

    play = 'Lets play guess the number to start guess a number between 1 and 10: ' + name
    print(play)
    secret = random.randint(1, 10)
    auto_win = int(1234)
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
                print('Incorrect try again')
        except ValueError:
            print('Please enter a number')
    play_again()


def play_again():
    again = input('would you like to play again ? or would you like to play something else ? (y/n/m): ').lower()

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
