import sys
# from guess_number_game import play_level, start_game, play_again
from pathlib import Path

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QLineEdit,
)



class GuessNumberGame(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Guess The Number')
        self.resize(450, 500)

        layout = QVBoxLayout()

        self.setLayout(layout)

        image_path = Path(__file__).parent / "Assets" / "images" / "depar.jpg"

        print(image_path)
        print(image_path.exists())

        self.setStyleSheet("""
            QWidget {
                background-image: url({image_path.as_posix()});
                background-repeat: no-repeat;
                background-position: center;
            }
        """)

app = QApplication(sys.argv)

window = GuessNumberGame()
window.show()


sys.exit(app.exec())
