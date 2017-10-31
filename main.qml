import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3

ApplicationWindow {
    visible: true
    width: 288
    height: 512
    color: "#f8f7ff"

    title: qsTr("Weather Station")

    Timer {
        id:timer
        interval: 1000; running: true; repeat: true
        onTriggered: time.text = felipe.name
        Component.onCompleted: timer.start()
    }

    Component {
        id: dataDelegate
        Item {
            width: grid.cellWidth; height: grid.cellHeight
            Rectangle {
                color: "#f8f7ff"
                anchors.leftMargin: 10
                anchors.fill: parent
                Image {
                    id: pic
                    source: icon;
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.leftMargin: 10
                }
                Text {
                    text: name;
                    anchors.horizontalCenter: parent.horizontalCenter;
                    anchors.verticalCenter: parent.verticalCenter;
                    font.pixelSize: 24
                    font.weight: Font.DemiBold
                }
            }
        }
    }

    GridView {
        id: grid
        anchors.fill: parent
        cellWidth: 360; cellHeight: 100
        flow: GridView.FlowTopToBottom

        model: DataModel {}
        delegate: dataDelegate
        focus: true

    }

    Text {
      id: time
    }
}


