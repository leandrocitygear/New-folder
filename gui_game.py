import sys
# from guess_number_game import play_level, start_game, play_again
from PyQt6.QtGui import QPixmap



from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QMainWindow
)



class GuessNumberGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Guess The Number')
        self.resize(400, 400)

        self.background = QLabel(self)
        
        # Load your image
        pixmap = QPixmap("Assets/images/imp2.jpg")
        self.background.setPixmap(pixmap)
        
        # Force the image to scale and fill the entire label area
        self.background.setScaledContents(True)

    def resizeEvent(self, event):
        # Dynamically resize the label to match the window size
        self.background.resize(self.size())
        super().resizeEvent(event)

app = QApplication(sys.argv)

window = GuessNumberGame()
window.show()


sys.exit(app.exec())
