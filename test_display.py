import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from thank_ui import Ui_MainWindow_alert

class MyApp(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow_alert()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())