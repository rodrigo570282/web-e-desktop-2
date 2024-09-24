from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap, QPainter, QImage
from PySide6.QtCore import Qt, QRect

class ImageLabel(QLabel):
    def __init__(self, image_path, text, parent=None):
        super().__init__(parent)
        self.image_path = image_path
        self.text = text
        self.pixmap = QPixmap(image_path)
        self.setPixmap(self.pixmap)
        self.setText(text)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("background: transparent; color: white; font-size: 20px; font-weight: bold;")

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self.pixmap())
        painter.setPen(Qt.white)
        painter.setFont(self.font())
        painter.drawText(QRect(0, 0, self.pixmap().width(), self.pixmap().height()), Qt.AlignCenter, self.text)
        self.setPixmap(self.pixmap())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Imagem com Texto")
        self.setGeometry(100, 100, 600, 400)
        layout = QVBoxLayout()

        # Caminho para a imagem e o texto que você deseja sobrepor
        image_path = "aula/corinthians.png"
        text = "Texto sobre a imagem"

        image_label = ImageLabel(image_path, text)
        layout.addWidget(image_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()