# This Python file uses the following encoding: utf-8
import os
import time
from pathlib import Path
import sys

import PySide2
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QLabel, QPushButton, QGridLayout, QWidget

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PySide2.QtCore import QSize

from deadline import Ui_Widget
from dwindow import Ui_DialogWindow
from PyQt5.QtWidgets import QScrollArea


class desciptionCor:
    def __init__(self):
        self.name = ''
        self.description = ''


class DialogWindow(QWidget):
    def __init__(self):
        super().__init__()
        window = QtWidgets.QVBoxLayout()
        self.ui = Ui_DialogWindow()
        self.ui.setupUi(self)
        window = self.window

    def closes(self):
        self.close()

    def open_window(self, message):
       self.ui.label.setText("Файл: " + message.name)
       self.ui.label.setStyleSheet("color:#fff; font-family:Montserrat; font-size: 13px")
       self.ui.label_2.setText("Признаки " + message.description)
       self.ui.label_2.setStyleSheet("color:#E23F5C;font-family:Montserrat; font-size: 15px")
       self.ui.pushButton.clicked.connect(self.closes)
       self.show()


class mywindow(QtWidgets.QMainWindow):
    documents = []
    results = []

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.upload.clicked.connect(self.upload_click)
        self.ui.launch.clicked.connect(self.launch_click)
        self.ui.clear_list.clicked.connect(self.removeAll)
        self.ui.clear_results.clicked.connect(self.clear_results)
        self.outputResults()
        self.w = None


    def upload_click(self):
        fname = QFileDialog.getOpenFileNames(self, "Загрузить документ(ы)", '.', "*.docx;")
        documentsGrid = self.ui.gridLayout
        self.documents = fname[0]

        documentsGrid.setRowStretch(len(self.documents), 1)

        for i in range(0, len(self.documents)):
            id = QLabel("#" + str(i + 1))
            id.setStyleSheet(
                "background: #4d4d4d;color:#fff;font-size:18px;\nborder-top-left-radius: 6px;\npadding-right:5px;\nborder-bottom-left-radius: 6;\n")
            file = open(self.documents[i], 'r')
            name = QLabel(file.name)
            size = QLabel("13")
            size.setStyleSheet("background: #4d4d4d;color:#fff;font-size:18px\n")
            buttonLaunch = QtWidgets.QPushButton()
            buttonRemove = QtWidgets.QPushButton()
            buttonRemove.clicked.connect(self.remove)
            buttonRemove.index = str(i)
            buttonRemove.setStyleSheet(
                "background: #4d4d4d; border: none; width: 60px; \nborder-top-right-radius: 6px;\nborder-bottom-right-radius: 6; padding: 5px;")

            buttonRemove.setIcon(QtGui.QIcon("close.png"))
            buttonLaunch.src = self.documents[i]
            buttonLaunch.clicked.connect(self.launchOnce)
            buttonLaunch.index = str(i)
            buttonLaunch.setStyleSheet("background: #4d4d4d; border: none; padding: 5px;")
            buttonLaunch.setIcon(QtGui.QIcon('launch.png'))

            name.setStyleSheet("background: #4d4d4d;color:#fff;font-size:18px\n")
            documentsGrid.addWidget(id, i, 0)
            documentsGrid.addWidget(name, i, 1)
            documentsGrid.addWidget(size, i, 2)
            documentsGrid.addWidget(buttonLaunch, i, 3)
            documentsGrid.addWidget(buttonRemove, i, 4)
            documentsGrid.setVerticalSpacing(10)
            w = QWidget()
            w.setLayout(documentsGrid)
            self.ui.scrollArea.setWidget(w)

    def launch_click(self):
        results = self.ui.verticalLayout

    def remove(self):
        index = int(self.sender().index)
        self.documents.pop(index)
        for i in range(0, 5):
            self.ui.gridLayout.itemAtPosition(index, i).widget().deleteLater()

    def removeAll(self):
        del self.documents[:]
        for i in reversed(range(self.ui.gridLayout.count())):
            self.ui.gridLayout.itemAt(i).widget().setParent(None)

    def launchOnce(self):
        print(self.sender().src)

    def outputResults(self):
        resultsBLock = self.ui.results
        self.results = [['0', 'Нормативно правовой акт', True], ['1', 'Нормативно правовой акт', False],['2', 'Нормативно правовой акт', True],['3', 'Нормативно правовой акт', True]]
        for i in range(len(self.results)):
            blockResult = QtWidgets.QHBoxLayout()
            id = QtWidgets.QLabel("#" + str(i))
            id.setStyleSheet("color:#fff; font-size:13px;")
            name = QtWidgets.QLabel(self.results[i][1])
            name.setStyleSheet("color:#fff;font-size:13px;")
            blockResult.addWidget(id)
            blockResult.addWidget(name)
            direction = None
            if (self.results[i][2] != True):
                status = QtWidgets.QLabel('Без факторов')
                status.setStyleSheet("color: #23EF5C;font-size:13px;")
                blockResult.addWidget(status)
            else:
                status = QtWidgets.QLabel("С факторами")
                status.setStyleSheet("color: #E23F5C;font-size:13px;")
                direction = QtWidgets.QPushButton("Подробнее")
                direction.setStyleSheet(
                    "background: transparent; border: 2px solid #fff; color: #fff;font-size:13px; padding-left:10px;padding-right:10px")
                direction.clicked.connect(self.openWindow)
                direction.name = self.results[i][1]
                direction.description = "\nЮридики-лингвистическая\nнеопределенность"
                blockResult.addWidget(status)

            blockResult.addWidget(direction if direction else QtWidgets.QLabel())
            resultsBLock.addLayout(blockResult)
        w = QWidget()
        w.setLayout(resultsBLock)
        self.ui.scrollArea_2.setWidget(w)

    def clear_results(self):
        del self.results[:]

        for i in range(self.ui.results.count()):
            existing_item = self.ui.results.takeAt(i)
            if existing_item:
                for j in range(0, existing_item.count()):
                    existing_item.itemAt(j).widget().setParent(None)
                    # existing_item.itemAt(j).deleteLater()


    def openWindow(self):
        self.w = DialogWindow()

        description = desciptionCor()
        description.name = self.sender().name
        description.description = self.sender().description

        self.w.open_window(description)

appStyle="""
QMainWindow{
background-color: darkgray;
}
"""
app = QtWidgets.QApplication([])
app.setStyleSheet("QMainWindow{background: #19FF5C;}")
app.setStyleSheet(appStyle)
application = mywindow()
application.show()

sys.exit(app.exec())
