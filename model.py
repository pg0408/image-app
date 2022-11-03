from random import choice
from os import listdir
from sys import exit
from PySide6.QtCore import QObject, Signal, Slot


class Model(QObject):

    def __init__(self):
        """
        initialises the model
        sets the attributes to initial values
        """
        super().__init__()
        self.files = listdir("images/")
        self.image = str()

    imageChanged = Signal(str, arguments=["file"])

    @Slot()
    def nextImage(self):
        """
        randomly picks a new image file
        """
        next_image = choice(self.files)
        self.image = f"images/{next_image}"
        self.imageChanged.emit(self.image)

    @Slot()
    def quit(self):
        """
        quits the application
        """
        exit()
