from PyQt5 import QtWidgets

from nitrokeyapp.qt_utils_mix_in import QtUtilsMixIn


class SetPinDialog(QtUtilsMixIn, QtWidgets.QDialog):
    def __init__(self, qt_app: QtWidgets.QApplication):
        QtWidgets.QDialog.__init__(self)
        QtUtilsMixIn.__init__(self)

        self.app = qt_app

    def init_set_pin(self):
        # dialogs
        self.new_pin = self.get_widget(QtWidgets.QLineEdit, "lineEdit_new_pin_set")
        self.confirm_new_pin = self.get_widget(
            QtWidgets.QLineEdit, "lineEdit_confirm_new_pin_set"
        )
        # self.buttons = self.get_widget(QtWidgets.QDialogButtonBox, "buttonBox")
        self.btn_ok = self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok)
        self.confirm_new_pin.textChanged.connect(self.same_pin)
        self.new_pin.textChanged.connect(self.same_pin)

    def same_pin(self):
        if self.new_pin.text() != self.confirm_new_pin.text():
            self.btn_ok.setEnabled(False)
        else:
            self.btn_ok.setEnabled(True)
