import sys
import time
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QLabel, QFrame, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
from main import asma


class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Spash Screen Example')
        self.setFixedSize(1100, 600)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.counter = 0
        self.n = 300  # total instance

        self.initUI()

        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(15)

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.frame = QFrame()
        layout.addWidget(self.frame)

        # center labels
        self.label = QLabel(self)
        self.pixmap = QPixmap('logo-admission.png')
        self.label.resize(self.width()-50, 200)
        self.label.move(20, 50)  # x, y
        self.label.setPixmap(self.pixmap)
        self.label.setAlignment(Qt.AlignCenter)

        self.labelDescription = QLabel(self.frame)
        self.labelDescription.resize(self.width() - 10, 50)
        self.labelDescription.move(0, self.label.y()+250)
        self.labelDescription.setObjectName('LabelDesc')
        self.labelDescription.setText('<strong>Initalizing</strong>')
        self.labelDescription.setAlignment(Qt.AlignCenter)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.resize(self.width() - 200 - 10, 50)
        self.progressBar.move(100, self.labelDescription.y() + 130)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setFormat('%p%')
        self.progressBar.setTextVisible(True)
        self.progressBar.setRange(0, self.n)
        self.progressBar.setValue(20)

        self.labelLoading = QLabel(self.frame)
        self.labelLoading.resize(self.width() - 10, 50)
        self.labelLoading.move(0, self.progressBar.y() + 70)
        self.labelLoading.setObjectName('LabelLoading')
        self.labelLoading.setAlignment(Qt.AlignCenter)
        self.labelLoading.setText('Created by Team ASMA')

    def loading(self):
        self.progressBar.setValue(self.counter)

        if self.counter == int(self.n * 0.2):
            self.labelDescription.setText(
                '<strong>Loading Function..</strong>')
        elif self.counter == int(self.n * 0.8):
            self.labelDescription.setText(
                '<strong>Loding UI..</strong>')
        elif self.counter >= self.n:
            self.timer.stop()
            self.close()

            time.sleep(1)

            asma()

        self.counter += 1


if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    app.setStyleSheet('''
        #LabelTitle {
            font-size: 60px;
            font-family: 'Roboto';
            color: black;
        }

        #LabelDesc {
            font-size: 30px;
            font-family: 'Roboto';
            color: black;
        }

        #LabelLoading {
            font-size: 30px;
            font-family: 'Roboto';
            color: black;
        }

        QFrame {
            background-color: white;
            color: black;
        }

        QProgressBar {
            background-color: #4C79C7;
            color: black;
            border-style: none;
            border-radius: 10px;
            text-align: center;
            font-size: 30px;
            font-family: 'Roboto';
        }

        QProgressBar::chunk {
            border-radius: 10px;
            background-color:#00D9F6;
        }
    ''')

    splash = SplashScreen()
    splash.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
