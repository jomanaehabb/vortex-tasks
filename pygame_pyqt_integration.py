import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer

class PygameIntegration(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pygame and PyQt5 Integration")
        
        # Pygame setup
        pygame.init()
        self.joystick = None
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()

        # PyQt5 setup
        self.label = QLabel("Press a key or joystick button!")
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Timer to poll Pygame events
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_pygame_events)
        self.timer.start(100)

    def check_pygame_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.label.setText(f"Key pressed: {pygame.key.name(event.key)}")
            elif event.type == pygame.JOYBUTTONDOWN and self.joystick:
                self.label.setText(f"Joystick button {event.button} pressed")

    def closeEvent(self, event):
        pygame.quit()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = PygameIntegration()
    mainWindow.show()
    sys.exit(app.exec_())
