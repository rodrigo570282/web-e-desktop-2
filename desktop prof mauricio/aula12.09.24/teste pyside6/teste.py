from PySide6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])
window = QWidget()
window.setWindowTitle("Minha Primeira Janela")
window.setGeometry(100, 100, 280, 80)
label = QLabel("Olá, PySide6!", parent=window)
window.show()
app.exec()