from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QFontComboBox
from PySide6.QtCore import Qt
import sys, random

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Adivina el numero')
        self.setFixedSize(300,250)
        self.interface()
        self.setStyleSheet("""
        QMainWindow{
        background-color:gray;
        }
        *{
        font-family:'Montserrat';
        }
        QPushButton{
        }""")
    def interface(self):

        title = QLabel("Adivina el numero by <a href='https://www.instagram.com/augusto_silva.py' style='text-decoration:none'>LucasAugusto</a>"); title.setAlignment(Qt.AlignCenter)

        choose_label = QLabel("Elige un numero del 1 al 100")
        self.choose_input = QLineEdit()
        choose_buton = QPushButton("Elegir")
        
        choose_hLayout=QHBoxLayout()
        choose_hLayout.addWidget(choose_label)
        choose_hLayout.addWidget(self.choose_input)
        choose_hLayout.addWidget(choose_buton)
        choose_hLayout_w = QWidget(); choose_hLayout_w.setLayout(choose_hLayout)

        self.label_result = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(choose_hLayout_w)
        layout.addWidget(self.label_result)
        widget = QWidget()

        widget.setLayout(layout)
        self.setCentralWidget(widget)

        choose_buton.clicked.connect(self.choose)

    def choose(self):
        random_number = random.randint(0, 101)
        number = self.choose_input.text()
        try:
            number = int(number)
        except:
            self.label_result.setText('No ingresaste un numero')
        if number == random_number:
            self.label_result.setText(f'El numero escogido fue: {random_number}\nTu escogiste: {number}\n Ganaste!! ')
        else:
            self.label_result.setText(f'El numero escogido fue: {random_number}\nTu escogiste: {number}\n Intentalo otra vez!! ')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())