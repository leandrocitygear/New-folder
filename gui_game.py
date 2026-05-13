import sys
# from guess_number_game import play_level, start_game, play_again
from PyQt6.QtGui import QPixmap
from pathlib import Path
import random
from PyQt6.QtCore import QTimer

# import play_song



from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QMainWindow
)


# play_song.play_game_song()

class GuessNumberGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Guess The Number')
        self.resize(400, 400)

        self.image_folder = Path(__file__).parent / "Assets" / "images"


        self.background_images = [
            self.image_folder / "dep2.jpg",
            self.image_folder / "depar.jpg",
            self.image_folder / "imp1.jpg",
            self.image_folder / "imp2.jpg",
            self.image_folder / "db.webp",
        ]


        self.background = QLabel(self)
        
        # Load your image
        self.current_image = None
        self.change_background()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.change_background)
        self.timer.start(5000)

        self.background.setScaledContents(True)
        # Force the image to scale and fill the entire label area

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

app = QApplication(sys.argv)

window = GuessNumberGame()
window.show()


sys.exit(app.exec())
