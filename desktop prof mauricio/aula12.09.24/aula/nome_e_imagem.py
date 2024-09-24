import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Criando o widget principal e o layout
    window = QWidget()
    layout = QVBoxLayout(window)

    # Criando o QLabel para o texto
    text_label = QLabel("Hello World", alignment=Qt.AlignCenter)
    text_label.setStyleSheet("font-size: 24px; font-weight: bold;")

    # Criando o QLabel para a imagem
    image_label = QLabel()
    pixmap = QPixmap("aula/corinthians.png")  # Substitua pelo caminho da sua imagem
    image_label.setPixmap(pixmap)
    image_label.setAlignment(Qt.AlignCenter)

    # Adicionando os QLabel ao layout
    layout.addWidget(text_label)
    layout.addWidget(image_label)

    # Configurando o layout e exibindo a janela
    window.setLayout(layout)
    window.setWindowTitle("Texto e Imagem")
    window.resize(400, 300)
    window.show()

    sys.exit(app.exec())