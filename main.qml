import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.3

ApplicationWindow {
    visible: true
    width: 360
    height: 640
    title: qsTr("Weather Station")

    Timer {
        id:timer
        interval: 1000; running: true; repeat: true
        onTriggered: list.get(0).value += 1
        Component.onCompleted: timer.start()
    }


    Column {
        spacing: 2

        GridView {
            width: 450; height: 400
            flow: GridView.FlowTopToBottom

            model: DataModel {}
            delegate: Column {
                Image { source: icon; anchors.centerIn: parent.centerIn }
                Text { text: name; }
            }
        }

    }


    Text {
      anchors.bottom : parent.bottom
      text:felipe.name
    }
}
