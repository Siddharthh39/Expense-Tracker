# to call everything 

import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from app import Expense

def main():
    app = QApplication(sys.argv)

    window = Expense()
    window.show

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
