import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import pygame

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()

        # Inicializa o mixer do pygame
        pygame.mixer.init()

        # Configura a interface gráfica
        self.init_ui()

    def init_ui(self):
        # Cria o botão para tocar a música
        self.play_button = QPushButton('Play Music', self)
        self.play_button.clicked.connect(self.play_music)

        # Configura o layout
        layout = QVBoxLayout()
        layout.addWidget(self.play_button)
        self.setLayout(layout)

        # Configura a janela principal
        self.setWindowTitle('Music Player')
        self.setGeometry(300, 300, 200, 100)

    def play_music(self):
        # Caminho para o arquivo de música
        music_file = 'aula17.09.24/hino-do-corinthians.mp3'

        # Carrega e toca a música
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec())