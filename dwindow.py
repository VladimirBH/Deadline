# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testqq.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogWindow(object):
    def setupUi(self, DialogWindow):
        DialogWindow.setObjectName("DialogWindow")
        DialogWindow.resize(300, 300)
        DialogWindow.setStyleSheet("background: #383838;")
        self.pushButton = QtWidgets.QPushButton(DialogWindow)
        self.pushButton.setGeometry(QtCore.QRect(99, 246, 102, 37))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color: #000; background-color: #19FF5A; border-radius: 7px;")
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(DialogWindow)
        self.frame.setGeometry(QtCore.QRect(11, 17, 279, 209))
        self.frame.setStyleSheet("font-size: 18px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 241, 51))
        self.label.setStyleSheet("font-size: 18px")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 251, 131))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(DialogWindow)
        QtCore.QMetaObject.connectSlotsByName(DialogWindow)

    def retranslateUi(self, DialogWindow):
        _translate = QtCore.QCoreApplication.translate
        DialogWindow.setWindowTitle(_translate("DialogWindow", "???????????????? ???????????????????? ???? ?????????????????? by DeadLine"))
        self.pushButton.setText(_translate("DialogWindow", "OK"))
        self.label.setText(_translate("DialogWindow", "????????: "))
        self.label_2.setText(_translate("DialogWindow", "????????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogWindow = QtWidgets.QWidget()
    ui = Ui_DialogWindow()
    ui.setupUi(DialogWindow)
    DialogWindow.show()
    sys.exit(app.exec_())
