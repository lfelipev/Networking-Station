import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    Timer {
        id:timer
        interval: 1000; running: true; repeat: true
        onTriggered: list.get(0).value += 1
        Component.onCompleted: timer.start()
    }

    GridView {
        anchors.fill: parent
        model: ListModel {
            id:list
            ListElement { value : 0 }
            ListElement { value : 0 }
            ListElement { value : 0 }
            ListElement { value : 0 }
            ListElement { value : 0 }
            ListElement { value : 0 }
            ListElement { value : 0 }
            ListElement { value : 0 }
            ListElement { value : 0 }
            ListElement { value : 0 }
        }

        delegate: Rectangle {
            width: 60; height: 60
            color: "Blue"

            Label {
                anchors.centerIn: parent
                text:value
            }
        }
    }

    Text {
      anchors.bottom : parent.bottom
      text:felipe.name
    }
}
