import QtQuick
import QtQuick.Controls

ApplicationWindow {
    visible: true
    width: 600 
    height: 600
    title: "Image App"
    property string filename: ""
    property QtObject model

    Image {
        id: image
        sourceSize.width: parent.width
        sourceSize.height: parent.height
        source: filename
        height: parent.height - (2 * nextButton.height)
        width: parent.width
        fillMode: Image.PreserveAspectFit
    }

    Button {
        id: nextButton
        text : "Next image"
        y: image.height
        onClicked: model.nextImage()
        width: parent.width
    }

    Button {
        id: quitButton
        text : "Quit application"
        y: image.height + nextButton.height
        onClicked: model.quit()
        width: parent.width
    }

    Connections {
        target: model
        function onImageChanged(filename) {
            image.source = filename;
            image.reload
        }
    }
}
