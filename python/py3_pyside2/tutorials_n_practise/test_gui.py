import sys

from PySide2 import QtGui
from PySide2 import QtCore

from PySide2 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

gajanan = QtWidgets.QPushButton('Shree Gajanan Prasanna.')

gajanan.resize(100, 21)

gajanan.show()

sys.exit(app.exec_())