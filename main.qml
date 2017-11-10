import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3

ApplicationWindow {
    visible: true
    width: 288
    height: 512
    color: "#f8f7ff"

    property var data

    title: qsTr("Weather Station")

    function updateData() {
        data = status.getData
        temperature.text = status.temperature
        humidity.text = status.humidity
        luminosity.text = status.luminosity
        rain.text = status.rain
        density.text = status.density
    }

    Timer {
        id:timer
        interval: 1000; running: true; repeat: true
        onTriggered: updateData()
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
            name: "25"
            icon: "pics/thermometer.png"
        }
        ListElement {
            name: "89%"
            icon: "pics/drop.png"
        }
        ListElement {
            name: "94%"
            icon: "pics/contrast.png"
        }
        ListElement {
            name: "24%"
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


