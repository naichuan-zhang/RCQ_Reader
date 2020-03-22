# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os
import time
import urllib.request

from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem, QListWidgetItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lv_state = QtWidgets.QGroupBox(self.centralwidget)
        self.lv_state.setGeometry(QtCore.QRect(40, 10, 711, 241))
        self.lv_state.setStyleSheet("edi")
        self.lv_state.setObjectName("lv_state")
        self.label = QtWidgets.QLabel(self.lv_state)
        self.label.setGeometry(QtCore.QRect(40, 40, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.lv_state)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.lv_state)
        self.label_3.setGeometry(QtCore.QRect(360, 40, 161, 16))
        font = QtGui.QFont()
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:red")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        self.lineEdit_path = QtWidgets.QLineEdit(self.lv_state)
        self.lineEdit_path.setGeometry(QtCore.QRect(170, 100, 301, 21))
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.lineEdit_choose = QtWidgets.QLineEdit(self.lv_state)
        self.lineEdit_choose.setGeometry(QtCore.QRect(170, 40, 113, 21))
        self.lineEdit_choose.setObjectName("lineEdit_choose")
        self.pushButton_select = QtWidgets.QPushButton(self.lv_state)
        self.pushButton_select.setGeometry(QtCore.QRect(520, 100, 93, 28))
        self.pushButton_select.setObjectName("pushButton_select")
        self.pushButton_ok = QtWidgets.QPushButton(self.lv_state)
        self.pushButton_ok.setGeometry(QtCore.QRect(510, 190, 93, 28))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(40, 280, 711, 261))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 711, 231))
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 711, 231))
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # binding button click listeners
        self.pushButton_select.clicked.connect(self.on_select_path_clicked)
        self.pushButton_ok.clicked.connect(self.on_ok_clicked)
        self.listWidget.clicked.connect(self.on_item_clicked)
        self.tableWidget.clicked.connect(self.on_table_clicked)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lv_state.setTitle(_translate("MainWindow", "抓取设置"))
        self.label.setText(_translate("MainWindow", "请选择抓取期数："))
        self.label_2.setText(_translate("MainWindow", "请选择保存路径："))
        self.label_3.setText(_translate("MainWindow", "注：期数范围为01-24"))
        self.pushButton_select.setText(_translate("MainWindow", "选择"))
        self.pushButton_ok.setText(_translate("MainWindow", "确定"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "期数"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "名称"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "按期数显示"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "按名称显示"))
        # set default date to current date (YYYY-MM)
        date = str(time.localtime().tm_year) + '-' + str(time.localtime().tm_mon)
        self.lineEdit_choose.setText(date)
        # set default path to current project directory
        self.lineEdit_path.setText(_translate("MainWindow", os.getcwd()))

    def on_select_path_clicked(self):
        """select path button clicked listener"""
        try:
            self.file_path = QFileDialog.getExistingDirectory(None, "Choose File", os.getcwd())
            self.lineEdit_path.setText(self.file_path)
        except Exception as e:
            print(e)

    def on_ok_clicked(self):
        try:
            # while True:
                self.date = self.lineEdit_choose.text()
                year, month = self.date.split('-')
                self.base_url = f'http://www.52dzxy.com/{year}_{month}/'
                urlList = self.base_url + 'index.html'
                self.get_data(urlList, self.lineEdit_path.text())
        except Exception as e:
            print(e)
        self.get_files()
        self.bind_list()
        self.bind_table()

    def get_files(self):
        self.list = os.listdir(self.lineEdit_path.text() + "\\"
                               + self.lineEdit_choose.text())

    def bind_list(self):
        for i in range(0, len(self.list)):
            self.item = QListWidgetItem(self.listWidget)
            self.item.setIcon(QtGui.QIcon('note.ico'))
            self.item.setText(str(self.list[i])[0:5] + '...')
            self.item.setToolTip(self.list[i])
            self.item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

    def bind_table(self):
        for i in range(0, len(self.list)):
            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(self.lineEdit_choose.text()))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(self.list[i]))

    def on_table_clicked(self, item: QTableWidgetItem):
        path = self.lineEdit_path.text() + '\\' + self.lineEdit_choose.text() + '\\' + item.text()
        print(path)
        # os.startfile(path)

    def on_item_clicked(self, item: QTableWidgetItem):
        path = self.lineEdit_path.text() + '\\' + self.lineEdit_choose.text() + '\\' + item.toolTip()
        print(path)
        # os.startfile(path)

    def get_data(self, url, path):
        """get data obtained from specific url, and save it as a file"""
        soup = self.url_to_soup(url)
        a_list = soup.select('.maglisttitle a')
        path = path + "\\" + self.date + "\\"
        if not os.path.isdir(path):
            os.mkdir(path)
        for item in a_list[:5]:
            article_url = self.base_url + item['href']
            print(article_url)
            article_soup = self.url_to_soup(article_url)
            title = str(article_soup.find('h1')).lstrip('<h1>').rstrip('</h1>')
            author = str(article_soup.find(id='pub_date')).strip()
            filename = path + title + '.txt'
            file = open(filename, 'w')
            file.write('<<' + title + '>>\n\n')
            file.write(author + '\n\n')
            content = article_soup.select('.blkContainerSblkCon p')
            for c in content:
                text = c.text
                file.write(text)
            file.close()
        QMessageBox.information(None, "Message", 'The article of ' +
                                self.date + ' has been saved successfully!', QMessageBox.Ok)

    def url_to_soup(self, url):
        """extract data from url"""
        # open url
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        return soup
