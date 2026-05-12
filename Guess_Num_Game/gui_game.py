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
        self.resize(450, 500)

        layout = QVBoxLayout()

        self.setLayout(layout)

app = QApplication(sys.argv)

window = GuessNumberGame()
window.show()

# window = QWidget()
# window.resize(800, 500)
window.setStyleSheet("""
    QWidget {
        background-image: url(71rq+laPZIL._UF1000,1000_QL80_.jpg);
        background-repeat: no-repeat;
        background-position: center;
    }
""")

sys.exit(app.exec())
