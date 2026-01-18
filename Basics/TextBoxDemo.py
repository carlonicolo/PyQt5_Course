import sys

from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget


def main():
    app = QApplication(sys.argv)

    widget = QWidget()

    namelabel = QLabel(widget)
    namelabel.move(20, 50)
    namelabel.setText("Enter your name")

    name = QLineEdit(widget)
    name.move(160, 50)

    submit = QPushButton(widget)
    submit.setText("Submit")
    submit.move(180, 80)


    widget.setGeometry(50,50,520,300)
    widget.setWindowTitle("LineEdit Demo Application")
    widget.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()