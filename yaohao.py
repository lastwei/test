import json
import sys
import traceback
import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(800, 600)
        self.lineEdit = QtWidgets.QLineEdit(Widget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(180, 10, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 10, 121, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(Widget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 10, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(Widget)
        self.tableWidget.setGeometry(QtCore.QRect(335, 41, 281, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(139)
        self.tableWidget_2 = QtWidgets.QTableWidget(Widget)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 40, 141, 251))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(139)
        self.pushButton_3 = QtWidgets.QPushButton(Widget)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 40, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Widget)
        self.pushButton_4.setGeometry(QtCore.QRect(590, 10, 81, 31))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "骗傻逼"))
        self.pushButton.setText(_translate("Widget", "录入"))
        self.pushButton_2.setText(_translate("Widget", "抽"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Widget", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Widget", "楼层"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Widget", "存量"))
        self.pushButton_3.setText(_translate("Widget", "删除"))
        self.pushButton_4.setText(_translate("Widget", "删除"))


        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.loucen = []
        self.pushButton.clicked.connect(self.luru)
        self.pushButton_3.clicked.connect(self.delete)
        self.pushButton_2.clicked.connect(self.chou)
        self.pushButton_4.clicked.connect(self.delete1)
        self.houtai_name = []
        self.houtai_loucen = []
        self.houtai()
    def houtai(self):
        with open("haha.json") as f:
            result = json.load(f)
            for i in result:
                self.houtai_name.append(i)
                self.houtai_loucen.append(result[i])

    def luru(self):
        loucen = self.lineEdit.text()
        self.num = self.tableWidget_2.rowCount()
        self.tableWidget_2.setRowCount(self.num + 1)
        NewItem = QtWidgets.QTableWidgetItem(str(loucen))
        self.tableWidget_2.setItem(self.num,0, NewItem)
    def delete(self):
        for i in  self.tableWidget_2.selectedItems():
            self.tableWidget_2.removeRow(i.row())
    def delete1(self):
        for i in  self.tableWidget.selectedItems():
            self.tableWidget.removeRow(i.row())
    def chou(self):
        self.loucen.clear()
        try:
            for i in range(self.num+1):
                loucen = self.tableWidget_2.item(i,0).text()
                self.loucen.append(loucen)
            name = self.lineEdit_2.text()
            index = random.randrange(0,len(self.loucen))
            loucen = self.loucen[index]
            if name in self.houtai_name:
                print(self.houtai_name.index(name))
                a = self.houtai_loucen[self.houtai_name.index(name)].split(",")
                print(a)
                index = random.randrange(0, len(a))
                loucen = a[index]
            else:
                    for i in self.houtai_loucen:
                        while loucen in i:
                            index = random.randrange(0, len(self.loucen))
                            loucen = self.loucen[index]
                        else:
                            break
            self.num1 = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(self.num1 + 1)
            NewItem = QtWidgets.QTableWidgetItem(str(loucen))
            newname = QtWidgets.QTableWidgetItem(str(name))
            self.tableWidget.setItem(self.num1, 1, NewItem)
            self.tableWidget.setItem(self.num1, 0, newname)
            if loucen in self.loucen:
                a = self.loucen.index(loucen)
                self.tableWidget_2.removeRow(a)
                self.num-=1
        except:
            traceback.print_exc()
            pass
if __name__ == "__main__":
    application = QApplication(sys.argv)  # 窗口通讯
    MainWindow = QtWidgets.QMainWindow()
    root = Ui_Widget()  # 创建对象
    root.setupUi(MainWindow)
    MainWindow.show()  # 展示窗口
    sys.exit(application.exec_())  # 消息循环