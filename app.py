# full main app
from PyQt6.QtWidgets import(
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QDateEdit,
    QTabWidget,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QTableWidgetItem,
    QHeaderView,
)

from PyQt6.QtCore import(
    QDate
    # Qt
)

class Expense(QWidget):
    
    def __init__(self):
        super().__init__()
        self.settings()

    def settings(self):
        self.setGeometry(750, 300, 550, 500)
        self.setWindowTitle("Expense Tracker")