import sys
import cv2
import threading
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt

class WebcamViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Webcam Viewer")
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)
        self.capture = cv2.VideoCapture(0)
        self.is_running = True
        self.thread = threading.Thread(target=self.update_frame)
        self.thread.start()

    def update_frame(self):
        while self.is_running:
            ret, frame = self.capture.read()
            if ret:
                # Convert frame to RGB format
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_frame.shape
                bytes_per_line = ch * w
                image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                self.image_label.setPixmap(QPixmap.fromImage(image))

    def closeEvent(self, event):
        self.is_running = False
        self.thread.join()
        self.capture.release()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = WebcamViewer()
    viewer.show()
    sys.exit(app.exec_())
