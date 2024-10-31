import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.initUI()

    def initUI(self):
        # Display
        self.display = QLineEdit(self)
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(35)

        # Button layout
        buttons = {
            '7': (0, 0), '8': (0, 1), '9': (0, 2), '/': (0, 3),
            '4': (1, 0), '5': (1, 1), '6': (1, 2), '*': (1, 3),
            '1': (2, 0), '2': (2, 1), '3': (2, 2), '-': (2, 3),
            '0': (3, 0), '.': (3, 1), '=': (3, 2), '+': (3, 3),
        }

        grid_layout = QGridLayout()
        for text, pos in buttons.items():
            button = QPushButton(text)
            button.clicked.connect(self.on_button_clicked)
            grid_layout.addWidget(button, *pos)

        # Set main layout
        layout = QVBoxLayout()
        layout.addWidget(self.display)
        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def on_button_clicked(self):
        button_text = self.sender().text()
        
        if button_text == "=":
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText("Error")
        elif button_text == "C":
            self.display.clear()
        else:
            self.display.setText(self.display.text() + button_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
