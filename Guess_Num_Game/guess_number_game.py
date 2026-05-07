from datetime import date
import random
date = date.today()
formatted_date = date.strftime("%B %d, %Y")

# count = 0

# def counter():
#     global count
#     count += 1
#     return count

player_ids = list(range(1, 100001))


player_id = random.choice(player_ids)

name = str(input('Enter your name: '))
age = int(input('Enter your Age: '))
location = str(input('Where do you live: '))
welcome = 'Welcome to Guess the number Game ' + name 

if age < 18:
    print('too young')

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
    while True:
        try:
            guess = int(input('enter a number: '))
            if guess == secret:
                print('correct')
                print('You win: ' + name)
                break
            else:
                print('Incorrect try again')
        except ValueError:
            print('Please enter a number')
    play_again()


def play_again():
    print('Type [1 for yes] or [0 for no]')
    again = input('would you like to play again (y/n): ').lower()
    try:
        
        if again == 'y':
            return start_game()
        else:
            print('game over')

    except ValueError:
        print('please enter (y/n): ')
start_game()
