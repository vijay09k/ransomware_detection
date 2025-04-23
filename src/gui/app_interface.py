from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from automation.ransomware_simulation import RansomwareSimulator
from config import CHROME_DRIVER_PATH

class RansomwareApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Ransomware Detection App")
        layout = QVBoxLayout()

        # URL input
        self.url_label = QLabel("Enter URL to Scan:")
        layout.addWidget(self.url_label)

        self.url_input = QLineEdit()
        layout.addWidget(self.url_input)

        # Scan button
        self.scan_button = QPushButton("Scan")
        self.scan_button.clicked.connect(self.scan_url)
        layout.addWidget(self.scan_button)

        # Result display
        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def scan_url(self):
        url = self.url_input.text()
        simulator = RansomwareSimulator(driver_path=CHROME_DRIVER_PATH)
        simulator.simulate_attack(url)
        self.result_label.setText("Simulation completed. Check logs for details.")
