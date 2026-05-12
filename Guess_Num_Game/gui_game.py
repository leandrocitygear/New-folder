import sys
# from guess_number_game import play_level, start_game, play_again

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
        self.resize(400, 450)

        layout = QVBoxLayout()

        self.setLayout(layout)

app = QApplication(sys.argv)

window = GuessNumberGame()
window.show()

sys.exit(app.exec())
