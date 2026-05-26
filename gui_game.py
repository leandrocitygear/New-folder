import sys
# from guess_number_game import play_level, start_game, play_again
from PyQt6.QtGui import QPixmap
from pathlib import Path
import random
from PyQt6.QtCore import QTimer

import play_song
from guess_number_game import GameLogic



from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QMainWindow
)


play_song.play_game_song()

class GuessNumberGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Guess The Number')
        self.resize(400, 400)



        self.start_button = QPushButton("Start Game", self)
        self.start_button.setGeometry(125, 140, 150, 40)
        self.start_button.clicked.connect(self.start_game)
        self.start_button.raise_()

        self.play_again_button = QPushButton("Play Again", self)
        self.play_again_button.setGeometry(125, 240, 150, 40)
        self.play_again_button.clicked.connect(self.start_game)
        self.play_again_button.hide()
        self.play_again_button.raise_()

        self.name_label = QLabel("Enter Your Name:", self)
        self.name_label.setGeometry(125, 100, 200, 30)
        self.name_label.setStyleSheet("color: black; font-size: 18px;")
        self.name_label.hide()

        self.name_input = QLineEdit(self)
        self.name_input.setGeometry(100, 140, 200, 40)
        self.name_input.hide()

        self.info_label = QLabel("Enter a Number", self)
        self.info_label.setGeometry(125, 100, 200, 30)
        self.info_label.hide()
        
        self.level_label = QLabel(self)
        self.level_label.setGeometry(125, 70, 200, 30)
        self.level_label.hide()

        self.guess_input = QLineEdit(self)
        self.guess_input.setGeometry(100, 140, 200, 40)
        self.guess_input.hide()

        self.result_label = QLabel("", self)
        self.result_label.setGeometry(125, 200, 200, 40)
        self.result_label.hide()
   

        self.image_folder = Path(__file__).parent / "Assets" / "images"


        self.background_images = [
            self.image_folder / "dep2.jpg",
            self.image_folder / "depar.jpg",
            self.image_folder / "imp1.jpg",
            self.image_folder / "imp2.jpg",
            self.image_folder / "db.webp",
        ]


        self.background = QLabel(self)
        self.background.lower()
        
        # Load your image
        self.current_image = None
        self.change_background()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.change_background)
        self.timer.start(20000)

        self.result_timer = QTimer(self)
        self.result_timer.setSingleShot(True)
        self.result_timer.timeout.connect(self.result_label.hide)

        self.background.setScaledContents(True)
        # Force the image to scale and fill the entire label area

    def start_game(self):

        self.start_button.hide()

        self.name_label.show()
        self.name_input.show()

        self.name_input.returnPressed.connect(self.setup_game)


    def setup_game(self):

       if not hasattr(self, "game"):

        player_name = self.name_input.text().strip()

        if not player_name:
            return

        self.player_name = player_name

        self.game = GameLogic(player_name)

        # Hide name input
        self.name_label.hide()
        self.name_input.hide()


        # Show game widgets
        self.info_label.show()
        self.guess_input.show()
        self.result_label.show()
        self.level_label.show()


        level_info = self.game.get_level_info()
        

        self.level_label.setText(
            f"{level_info['level_name']} | "
            f"Guess {level_info['min']} - {level_info['max']}"
        )

        

        self.guess_input.returnPressed.connect(self.submit_guess)
        self.play_again_button.hide()

    def play_again(self):

        self.game = GameLogic(self.player_name)

        self.guess_input.show()
        self.level_label.show()
        self.info_label.show()

        self.setup_game()

    def submit_guess(self):

        guess_text = self.guess_input.text().strip()

        if not guess_text.isdigit():
            self.result_label.setText("Enter a valid number!")
            self.result_label.show()
            self.result_timer.start(3000)
            return

        guess = int(guess_text)

        result = self.game.check_guess(guess)

        self.result_label.setText(result["message"])
        self.result_label.show()
        self.result_timer.start(3000)

        if result["status"] == "next_level":

            level_info = self.game.get_level_info()

            self.level_label.setText(
                f"{level_info['level_name']} | "
                f"Guess {level_info['min']} - {level_info['max']}"
            )

        elif result["status"] in ["lose", "game_complete"]:

            self.guess_input.hide()
            self.level_label.hide()
            self.info_label.hide()
            self.play_again_button.show()

        self.guess_input.clear()
    

    def change_background(self):

        chosen_image = random.choice(self.background_images)

        while chosen_image == self.current_image and len(self.background_images) > 1:
            chosen_image = random.choice(self.background_images)

        self.current_image = chosen_image

        pixmap = QPixmap(str(chosen_image))

        self.background.setPixmap(pixmap)

    def resizeEvent(self, event):
        # Dynamically resize the label to match the window size
        self.background.resize(self.size())
        super().resizeEvent(event)

    def closeEvent(self, event):
        play_song.stop_music()
        event.accept()


app = QApplication(sys.argv)

window = GuessNumberGame()
window.show()


sys.exit(app.exec())
