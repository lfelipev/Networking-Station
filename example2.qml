Rectangle {

        width: 640; height: 480
        color: "Blue"
        border.width: 10

        GridView {
            width: 450; height: 400
            flow: GridView.FlowTopToBottom
            displayMarginBeginning: 40

            model: DataModel {}
            delegate: Column {
                Image { source: icon; anchors.centerIn: parent.centerIn }
                Text { text: name; }
            }
        }

    }
