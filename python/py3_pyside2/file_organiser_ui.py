import os, sys
from PySide2 import QtCore, QtGui, QtWidgets, QtUiTools


class AppWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        # self.input_files = QtWidgets.QFileDialog
        self.setupUI()
        self.resetValues()


    def setupUI(self):
        # Load UI and set it as main layout
        ui_file_path = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'PCBOutlineCreator.ui')
        main_widget = load_ui(ui_file_path, self)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(main_widget)
        self.setLayout(layout)

        # Get a reference to all required widgets
        self.input_file_edit = self.findChild(QtWidgets.QLineEdit, 'InputLineEdit')
        # self.input_button = self.findChild(QtGui.QToolButton, 'InputFileButton')
        self.input_button = self.findChild(QtWidgets.QPushButton, 'InputFileButton')
        self.output_file_edit = self.findChild(QtWidgets.QLineEdit, 'OutputLineEdit')
        self.output_button = self.findChild(QtWidgets.QPushButton, 'inputFileButton')
        self.execute_button = self.findChild(QtWidgets.QPushButton, 'ExecuteButton')
        self.cancel_button = self.findChild(QtWidgets.QPushButton, 'CancelButton')

        # Connect slots/callbacks and signals
        self.execute_button.setEnabled(False)
        self.cornersCheckBox.stateChanged.connect(self.onCornersCheckBoxChangedState)
        self.saveButton.clicked.connect(self.onSaveButtonClicked)
        self.inputFileButton.clicked.connect(self.onInputFileButtonClicked)
        self.exportButton.clicked.connect(self.onExportButtonClicked)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    sys.exit(app.exec_())

def load_ui(file_name, where=None):
    """
    Loads a .UI file into the corresponding Qt Python object
    :param file_name: UI file path
    :param where: Use this parameter to load the UI into an existing class (i.e. to override methods)
    :return: loaded UI
    """
    loader = QtUiTools.QUiLoader()
    ui_file = QtCore.QFile(file_name)
    ui_file.open(QtCore.QFile.ReadOnly)
    ui = loader.load(ui_file, where)
    ui_file.close()
    return ui

class PCBOutlineCreator(QtWidgets.QWidget):

        # Connect slots/callbacks and signals
        self.cornersSpinBox.setEnabled(False)
        self.cornersCheckBox.stateChanged.connect(self.onCornersCheckBoxChangedState)
        self.saveButton.clicked.connect(self.onSaveButtonClicked)
        self.inputFileButton.clicked.connect(self.onInputFileButtonClicked)
        self.exportButton.clicked.connect(self.onExportButtonClicked)

    def onCornersCheckBoxChangedState(self, checked):
        self.cornersSpinBox.setEnabled(bool(checked))

    def onSaveButtonClicked(self):
        reply = QtGui.QMessageBox.question(parent=self, title='Attention',
                                           text='File will be overwritten.\nDo you still want to proceed?',
                                           buttons=QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                           defaultButton=QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            filename = self.inputFileLineEdit.text()
            length = self.lengthSpinBox.value()
            width = self.widthSpinBox.value()
            line_width = self.lineWidthSpinBox.value()
            rounded = self.cornersCheckBox.isChecked()
            corners_radius = self.cornersSpinBox.value()
            x = self.xSpinBox.value()
            y = self.ySpinBox.value()

            print "Values are: "
            print "Filename: %s" % filename
            print "Length: %.2f Width: %.2f" % (length, width)
            print "Line width: %.2f" % line_width
            if corners_radius:
                print "Corner radius: %.2f" % corners_radius
            print "x: %.2f y: %.2f" % (x, y)


    def onInputFileButtonClicked(self):
        filename, filter = QtGui.QFileDialog.getOpenFileName(parent=self, caption='Open file', dir='.', filter='Kicad PCB Files (*.kicad_pcb)')

        if filename:
            self.inputFileLineEdit.setText(filename)

    def onExportButtonClicked(self):
        filename, filter = QtGui.QFileDialog.getSaveFileName(parent=self, caption='Select output file', dir='.', filter='Kicad PCB Files (*.kicad_pcb)')

        if filename:
            if '.kicad_pcb' != filename[-10:]:
                filename += '.kicad_pcb'

            print filename, filter



if __name__ == '__main__':

    # Create Qt app
    app = QtGui.QApplication(sys.argv)

    # Create the widget and show it
    gui = PCBOutlineCreator()
    gui.show()

    # Run the app
    sys.exit(app.exec_())