import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3

ApplicationWindow {
    visible: true
    minimumWidth: 288
    minimumHeight: 512
    maximumWidth: 288
    maximumHeight: 512
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

        dataModel.setProperty(0, "name", temp + "ºC")
        dataModel.setProperty(1, "name", humd + "%")
        dataModel.setProperty(2, "name", lum)

        if(lum < 10) {
            dataModel.setProperty(2, "icon", "pics/dark.png")
        }
        else if (lum > 10 && lum < 200) {
            dataModel.setProperty(2, "icon", "pics/dim-light.png")
        }
        else if (lum > 200 && lum < 500) {
            dataModel.setProperty(2, "icon", "pics/medium-light.png")
        }
        else if (lum > 500 && lum < 800) {
            dataModel.setProperty(2, "icon", "pics/light.png")
        }
        else if (lum > 800) {
            dataModel.setProperty(2, "icon", "pics/very-light.png")
        }

        if(dens > 900 && dens < 1024) {
            dataModel.setProperty(3, "name", "No rain")
            dataModel.setProperty(3, "icon", "pics/no-rain.png")
        }
        else if(dens > 400 && dens < 900) {
            dataModel.setProperty(3, "name", "Rainy")
            dataModel.setProperty(3, "icon", "pics/rain.png")
        }
        else if(dens > 0 && dens < 400) {
            dataModel.setProperty(3, "name", "Heavy Rain")
            dataModel.setProperty(3, "icon", "pics/storm.png")
        }
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
                anchors.leftMargin: 30
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
            icon: "pics/dark.png"
        }
        ListElement {
            name: "..."
            icon: "pics/no-rain.png"
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
}