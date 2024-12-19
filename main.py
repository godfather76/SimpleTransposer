from GUI import main_app
import sys


def main():
    app = main_app.qt.QtWidgets.QApplication(sys.argv)
    window = main_app.MainWindow(app)
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
