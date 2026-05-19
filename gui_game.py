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
        self.start_button.setGeometry(125, 200, 150, 50)
        self.start_button.clicked.connect(self.start_game)
        self.start_button.raise_()

        self.name_label = QLabel("Enter Your Name:", self)
        self.name_label.setGeometry(120, 100, 200, 30)
        self.name_label.hide()

        self.name_input = QLineEdit(self)
        self.name_input.setGeometry(100, 140, 200, 40)
        self.name_input.hide()

        self.info_label = QLabel("Enter a Number", self)
        self.info_label.setGeometry(70, 200, 300, 40)
        self.info_label.hide()

        self.guess_input = QLineEdit(self)
        self.guess_input.setGeometry(100, 250, 200, 40)
        self.guess_input.hide()

        self.result_label = QLabel("", self)
        self.result_label.setGeometry(70, 300, 300, 40)
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
        self.timer.start(10000)

        self.background.setScaledContents(True)
        # Force the image to scale and fill the entire label area

    def start_game(self):

        self.start_button.hide()

        self.name_label.show()
        self.name_input.show()

        self.name_input.returnPressed.connect(self.setup_game)

    def setup_game(self):

        name = self.name_input.text().strip()

        if not name:
            return

        self.player_name = name

        # Create GameLogic object
        self.game = GameLogic(name)

        # Hide name input
        self.name_label.hide()
        self.name_input.hide()

        # Show game widgets
        self.info_label.show()
        self.guess_input.show()
        self.result_label.show()

        level_info = self.game.get_level_info()

        self.info_label.setText(
            f"{level_info['level_name']} | "
            f"Guess {level_info['min']} - {level_info['max']}"
        )

        self.guess_input.returnPressed.connect(self.submit_guess)

    def submit_guess(self):

        guess_text = self.guess_input.text().strip()

        if not guess_text.isdigit():
            self.result_label.setText("Enter a valid number!")
            return

        guess = int(guess_text)

        result = self.game.check_guess(guess)

        self.result_label.setText(result["message"])

        if result["status"] == "next_level":

            level_info = self.game.get_level_info()

            self.info_label.setText(
                f"{level_info['level_name']} | "
                f"Guess {level_info['min']} - {level_info['max']}"
            )

        elif result["status"] in ["lose", "game_complete"]:

            self.guess_input.setDisabled(True)

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
