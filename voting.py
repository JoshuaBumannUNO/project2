import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow
from logic import *

def main()->None:
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    window = QMainWindow()
    ui.setupUi(window)

    logic = Logic(ui)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()