import sys
import os
from PyQt5 import QtWidgets, QtGui, QtCore

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 350, 350)
        self.setWindowTitle('ClamAV')
        self.setWindowIcon(QtGui.QIcon('virus.png'))

        self.button1 = QtWidgets.QPushButton('Stop/Update/Start ClamAV')
        self.button1.clicked.connect(self.stop_update_start_clamav)

        self.button2 = QtWidgets.QPushButton('Status ClamAV')
        self.button2.clicked.connect(self.status_clamav)

        self.text = QtWidgets.QTextEdit()

        self.grid = QtWidgets.QGridLayout()
        self.grid.setSpacing(10)

        self.grid.addWidget(self.button1, 1, 0)
        self.grid.addWidget(self.button2, 2, 0)
        self.grid.addWidget(self.text, 3, 0, 5, 1)

        self.setLayout(self.grid)

        self.show()

    def stop_update_start_clamav(self):
        os.system('sudo systemctl stop clamav-freshclam')
        os.system('sudo freshclam')
        os.system('sudo systemctl start clamav-freshclam')

    def status_clamav(self):
        os.system('sudo systemctl status clamav-freshclam > /tmp/clamav.txt')
        self.text.setText(self.text.toPlainText() + '\n' + 'Status ClamAV:')
        with open('/tmp/clamav.txt', 'r') as f:
            data = f.read()
            self.text.setText(self.text.toPlainText() + '\n' + data)

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
