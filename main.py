from sys import exit
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from model import Model


def main():

    app = QGuiApplication([])
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('view.qml')
    model = Model()
    root = engine.rootObjects()[0]
    root.setProperty('model', model)
    model.nextImage()
    exit(app.exec())


if __name__ == "__main__":
    main()
