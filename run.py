import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from window import Ui_MainWindow


def main():
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
