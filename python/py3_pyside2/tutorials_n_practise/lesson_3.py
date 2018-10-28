import sys

from PySide2 import QtGui, QtCore, QtWidgets


app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
window.resize(200, 120)

quit_button = QtWidgets.QPushButton('Quit', window)
quit_button.setFont(QtGui.QFont('Times', 18, QtGui.QFont.Bold))
quit_button.setGeometry(10, 40, 180, 40)

QtCore.QObject.connect(quit_button, QtCore.SIGNAL('clicked()'),
                       app, QtCore.SLOT('quit()'))


window.show()
sys.exit(app.exec_())