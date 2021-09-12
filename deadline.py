# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1152, 720)
        Widget.setStyleSheet("background: #383838; font-size: 13px")
        self.upload = QtWidgets.QPushButton(Widget)
        self.upload.setGeometry(QtCore.QRect(20, 30, 203, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.upload.setFont(font)
        self.upload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.upload.setStyleSheet("background: #e23f5c; border: 1px solid transparent;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px\n"
"")
        self.upload.setObjectName("upload")
        self.launch = QtWidgets.QPushButton(Widget)
        self.launch.setGeometry(QtCore.QRect(215, 31, 183, 28))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.launch.setFont(font)
        self.launch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.launch.setStyleSheet("background: #19FF5A;\n"
"border-top-right-radius: 5px;\n"
"border-bottom-right-radius: 5px;")
        self.launch.setObjectName("launch")
        self.clear_list = QtWidgets.QPushButton(Widget)
        self.clear_list.setGeometry(QtCore.QRect(970, 31, 162, 26))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.clear_list.setFont(font)
        self.clear_list.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_list.setStyleSheet("color: #E23F5C; background: transparent; border: 2px solid #E23F5C; border-radius: 6px;")
        self.clear_list.setObjectName("clear_list")
        self.label_13 = QtWidgets.QLabel(Widget)
        self.label_13.setGeometry(QtCore.QRect(20, 80, 591, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: #fff; background: transparent; font-size: 24px")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Widget)
        self.label_14.setGeometry(QtCore.QRect(20, 510, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: #fff; background: transparent; font-size: 24px")
        self.label_14.setObjectName("label_14")
        self.frame = QtWidgets.QFrame(Widget)
        self.frame.setGeometry(QtCore.QRect(20, 550, 1112, 151))
        self.frame.setStyleSheet("background-color:rgb(76, 76, 76);\n"
"border-radius: 6px;\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.clear_results = QtWidgets.QPushButton(self.frame)
        self.clear_results.setGeometry(QtCore.QRect(5, 5, 182, 28))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.clear_results.setFont(font)
        self.clear_results.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_results.setStyleSheet("border: 2px solid #E23F5C; background: transparent; border-radius: 6px; color: #E23F5C;")
        self.clear_results.setAutoDefault(True)
        self.clear_results.setObjectName("clear_results")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 36, 1111, 81))
        self.scrollArea_2.setStyleSheet("background: transparent")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1111, 81))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 1111, 71))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.results = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.results.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.results.setContentsMargins(6, 0, 5, 0)
        self.results.setObjectName("results")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(716, 120, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background: transparent; font-size: 14px; color: #19FF5A;")
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(869, 120, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background: transparent; font-size: 14px; color: #E23F5C;")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(1000, 120, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background: transparent; font-size: 14px; color: #fff;")
        self.label_6.setObjectName("label_6")
        self.scrollArea = QtWidgets.QScrollArea(Widget)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QtCore.QRect(20, 110, 1121, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setSizeIncrement(QtCore.QSize(0, 0))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setEnabled(True)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1119, 389))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 159))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1101, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 15, 0, 15)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame.raise_()
        self.launch.raise_()
        self.clear_list.raise_()
        self.upload.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.scrollArea.raise_()

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Проверка документов на коррупцию by DeadLine"))
        self.upload.setText(_translate("Widget", "Добавить документ(ы)"))
        self.launch.setText(_translate("Widget", "Запустить проверку"))
        self.clear_list.setText(_translate("Widget", "Очистить список"))
        self.label_13.setText(_translate("Widget", "Загруженные Нормативно Правовые Акты"))
        self.label_14.setText(_translate("Widget", "Результаты проверки"))
        self.clear_results.setText(_translate("Widget", "Очистить результаты"))
        self.label_5.setText(_translate("Widget", "Без факторов: 6"))
        self.label_4.setText(_translate("Widget", "С факторами: 3"))
        self.label_6.setText(_translate("Widget", "Количество: 9"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Widget = QtWidgets.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())