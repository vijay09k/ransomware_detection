from gui.app_interface import RansomwareApp
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    window = RansomwareApp()
    window.show()
    app.exec_()
