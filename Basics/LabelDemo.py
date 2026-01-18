import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

def main():
    app = QApplication(sys.argv)

    widget = QWidget()
    text = QLabel(widget)
    text.setText("PyQt Application Test")
    fo = QFont()
    fo.setPointSize(42)
    text.setFont(fo)
    text.move(110,20)



    widget.setGeometry(50,50,1000,500)
    widget.setWindowTitle("Label Demo")
    widget.show()

    sys.exit(app.exec_())



if __name__ == '__main__':
    main()