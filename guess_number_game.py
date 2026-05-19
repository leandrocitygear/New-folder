import random

class GameLogic:

    def __init__(self, player_name):
        self.player_name = player_name

        self.levels = [
            ("LEVEL 1", 1, 3),
            ("LEVEL 2", 1, 6),
            ("LEVEL 3", 1, 10),
            ("LEVEL LEGENDARY", 1, 20)
        ]

        self.current_level_index = 0
        self.attempts_left = 3

        self.auto_win = 1234
        self.generate_secret_number()

    def generate_secret_number(self):
        level_name, min_num, max_num = self.levels[self.current_level_index]
        self.secret_number = random.randint(min_num, max_num)
        print('secret:', self.secret_number)

    def get_level_info(self):
        level_name, min_num, max_num = self.levels[self.current_level_index]

        return {
            "level_name": level_name,
            "min": min_num,
            "max": max_num,
            "attempts": self.attempts_left
        }

    def check_guess(self, guess):

        if guess == self.auto_win:
            return {
                "status": "win_game",
                "message": f"You used the auto win cheat, {self.player_name}!"
            } 
        
        if guess == self.secret_number:
            self.current_level_index += 1

            if self.current_level_index >= len(self.levels):
                return {
                    "status": "game_complete",
                    "message": f"congratulations {self.player_name}, you beat the game!"
                }
            
            self.attempts_left = 3
            self.generate_secret_number()

            return {
                "status": "game_complete",
                "message": "Correct! Moving to next level"
            }

        self.attempts_left -= 1
        if self.attempts_left <= 0:

            return {
                "status": "lose",
                "message": "Game Over!"
            }
        
        return {
            "status": "wrong",
            "message": f"Wrong! Attempts left: {self.attempts_left}"
        }

   

    # def play_again():
    #     while True:
    #         again = input('would you like to play again ? (y/n): ').lower()

    #         if again == 'y':
            
    #         elif again == 'n':
    #             print('Thank you for playing!')
    #             break
    #         else:
    #             print('please enter (y/n): ')

    # play_again()
