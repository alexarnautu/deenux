import QtQuick 2.2
import QtQuick.Window 2.0
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4
import QtQuick.Layouts 1.1

ApplicationWindow {
    id: hello_world
    visible: true
    width: 499
    height: 300
    title: "Hello World"
    x: (Screen.width - width) / 2
    y: (Screen.height - height) / 2


    ColumnLayout {
        id: columnLayout1
        anchors.rightMargin: 10
        anchors.bottomMargin: 10
        anchors.leftMargin: 10
        anchors.topMargin: 10
        anchors.fill: parent
        spacing: 50
        visible: true

        Button {
            signal handler
            id: hello_button
            objectName: "hello_button"
            text: qsTr("Hello World!")
            Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            transformOrigin: Item.Center
            onClicked: handler()
            style: ButtonStyle {
                background: Rectangle {
                    implicitWidth: 100
                    implicitHeight: 25
                    border.width: control.activeFocus ? 2 : 1
                    border.color: "#FF0000"
                    radius: 0
                    gradient: Gradient {
                        GradientStop { position: 0 ; color: control.pressed ? "#ccc" : "#eee" }
                        GradientStop { position: 1 ; color: control.pressed ? "#aaa" : "#ccc" }
                    }
                }
            }
        }
    }
}
