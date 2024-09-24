import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configurar o layout principal
        self.layout = QVBoxLayout(self)

        # Criar QLabel para o texto
        self.text_label = QLabel("NÃO É SÓ FUTEBOL", alignment=Qt.AlignCenter)
        self.text_label.setStyleSheet("font-size: 24px; font-weight: bold;")

        # Criar QLabel para a imagem
        self.image_label = QLabel()
        self.pixmap = QPixmap("aula/corinthians.png")  # Imagem inicial
        self.image_label.setPixmap(self.pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)

        # Criar o botão para trocar a imagem
        self.change_image_button = QPushButton("Trocar Imagem")
        self.change_image_button.clicked.connect(self.change_image)

        # Adicionar widgets ao layout
        self.layout.addWidget(self.text_label)
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.change_image_button)

        # Configurar o widget principal
        self.setLayout(self.layout)
        self.setWindowTitle("Texto e Imagem com Botão")
        self.resize(400, 300)

        # Lista de imagens para alternar
        self.images = [
            "aula/corinthians.png",
            "aula/corinthians 2.png"
        ]
        self.current_image_index = 0

    def change_image(self):
        # Mudar a imagem para a próxima na lista
        self.current_image_index = (self.current_image_index + 1) % len(self.images)
        new_image_path = self.images[self.current_image_index]
        self.pixmap = QPixmap(new_image_path)
        self.image_label.setPixmap(self.pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

