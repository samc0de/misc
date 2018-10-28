import sys

from PySide2 import QtGui, QtCore, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(200, 120)
        self.quit_button = QtWidgets.QPushButton('Quit', self)
        self.quit_button.setGeometry(70, 40, 75, 30)
        self.quit_button.setFont(QtGui.QFont('Times', 18, QtGui.QFont.Bold))

        self.connect(self.quit_button, QtCore.SIGNAL('clicked()'),
                     QtWidgets.qApp, QtCore.SLOT('quit()'))


app = QtWidgets.QApplication(sys.argv)
widget = MyWidget()
widget.show()
sys.exit(app.exec_())