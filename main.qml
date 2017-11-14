import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3

ApplicationWindow {
    visible: true
    width: 288
    height: 512
    color: "#f8f7ff"

    property var data
    property var temp
    property var humd
    property var lum
    property var rainD
    property var dens

    title: qsTr("Weather Station")

    function updateStatus() {
        data = status.getData
        temp = status.temperature
        humd = status.humidity
        lum = status.luminosity
        rainD = status.rain
        dens = status.density
        dataModel.setProperty(0, "name", temp)
    }

    Timer {
        id:timer
        interval: 1000; running: true; repeat: true
        onTriggered: updateStatus()
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

    ListModel {
        id: dataModel

        ListElement {
            name: "..."
            icon: "pics/thermometer.png"
        }
        ListElement {
            name: "..."
            icon: "pics/drop.png"
        }
        ListElement {
            name: "..."
            icon: "pics/contrast.png"
        }
        ListElement {
            name: "..."
            icon: "pics/cloud.png"
        }
    }

    GridView {
        id: grid
        anchors.fill: parent
        cellWidth: 360; cellHeight: 100
        flow: GridView.FlowTopToBottom

        model: dataModel
        delegate: dataDelegate
        focus: true
    }

    Text {
        id: temperature
        topPadding: 10
    }

    Text {
        id: humidity
        topPadding: 20
    }

    Text {
        id: luminosity
        topPadding: 30
    }

    Text {
        id: rain
        topPadding: 40
    }

    Text {
        id: density
        topPadding: 50
    }
}


