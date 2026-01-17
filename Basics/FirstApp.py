import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

def main():
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.move(50, 50)
    widget.resize(400, 300)
    widget.setWindowTitle("First PyQt5 App")

    widget.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()