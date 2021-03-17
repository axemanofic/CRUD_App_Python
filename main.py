#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QDialog, QTableWidgetItem
from PyQt5 import uic
from TableUi import Ui_Table
from DialogUi import Ui_Dialog
import MySQLdb as mdb

groupDict = {'ИВТ' : 'direction_ivt', 'ИСТ' : 'direction_ist'}

class classDialog(QDialog, Ui_Dialog):
	enrollee = list()

	def __init__(self, group, function, tableWidget):
		QDialog.__init__(self)
		self.setupUi(self, function)
		self.function = function
		self.group = group

		if self.function == 'Изменение':
			self.tableWidget = tableWidget

			self.ID = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
			self.FIO = self.tableWidget.item(self.tableWidget.currentRow(), 1).text()
			self.POINTS = self.tableWidget.item(self.tableWidget.currentRow(), 2).text()
			self.ORIGINAL = self.tableWidget.item(self.tableWidget.currentRow(), 3).text()

			self.lineEdit_FIO.setText(self.FIO)
			self.lineEdit_Points.setText(self.POINTS)
			if self.ORIGINAL == '1':
				self.checkBoxOriginalDoc.setChecked(True)
			else:
				self.checkBoxOriginalDoc.setChecked(False)

		self.buttonBox.accepted.connect(lambda: self.acept_data())
		self.buttonBox.rejected.connect(lambda: self.reject_data())

	def acept_data(self):
		if self.function == 'Добавление':
			self.enrollee = (self.lineEdit_FIO.text(), self.lineEdit_Points.text(), self.checkBoxOriginalDoc.isChecked())
			print(self.enrollee)
			self.InsertData()
		else:
			self.enrollee = (self.lineEdit_FIO.text(), self.lineEdit_Points.text(), self.checkBoxOriginalDoc.isChecked(), self.ID);
			self.UpdateQuery()
		self.close();

	def reject_data(self):
		self.close()

	def InsertData(self):
		self.db = mdb.connect('localhost', 'axeman', 'axeman32rus', 'selection_committee')
		self.db.set_character_set('utf8')
		self.cursor = self.db.cursor()
		self.cursor.execute('SET NAMES utf8;')
		self.cursor.execute('SET CHARACTER SET utf8;')
		self.cursor.execute('SET character_set_connection=utf8;')

		query = "INSERT INTO " + groupDict[self.group] + " (`FIO`, `POINTS`, `ORIGINAL`) VALUES (%s, %s, %s)"

		self.cursor.execute(query, self.enrollee)
		self.db.commit()

	def UpdateQuery(self):
		self.db = mdb.connect('localhost', 'axeman', 'axeman32rus', 'selection_committee')
		self.db.set_character_set('utf8')
		self.cursor = self.db.cursor()
		self.cursor.execute('SET NAMES utf8;')
		self.cursor.execute('SET CHARACTER SET utf8;')
		self.cursor.execute('SET character_set_connection=utf8;')

		query = "UPDATE " + groupDict[self.group] + " SET FIO = %s, POINTS = %s, ORIGINAL = %s WHERE ID = %s"

		self.cursor.execute(query, self.enrollee)
		self.db.commit()



class classTable(QWidget, Ui_Table):
	group = str()
	flag = False
	def __init__(self, group):
		QWidget.__init__(self)
		self.setupUi(self, group)
		self.group = group
		self.show()
		self.SelectQuery()
		self.pushbtnInsert()
		self.pushbtnUpdate()
		self.pushbtnDelete()
		self.pushbtnClose()

	def pushbtnInsert(self):
		self.btnInsert.clicked.connect(lambda: self.WindowDialog_init('Добавление'))
	def pushbtnUpdate(self):
		self.btnUpdate.clicked.connect(lambda: self.WindowDialog_init('Изменение'))
	def pushbtnDelete(self):
		self.btnDelete.clicked.connect(lambda: self.DeleteQuery())
	def pushbtnClose(self):
		self.btnClose.clicked.connect(lambda: self.close())

	def WindowDialog_init(self, command):
		function = command

		self.id = self.GetEnrolleeId()

		if function == 'Изменение' and self.id == -1:
			QMessageBox.about(self, 'Ошибка', 'Вы не выбрали строку с данными')
			return
		self.dialog = classDialog(self.group, function, self.tableWidget)
		self.dialog.show()
		self.dialog.exec()
		self.SelectQuery()

	def ConnnectDB(self):
		try:
			self.db = mdb.connect('localhost', 'axeman', 'axeman32rus', 'selection_committee')
			self.db.set_character_set('utf8')
		except mdb.Error as e:
			QMessageBox.about(self, 'Ошибка', 'Ошибка соединения с базой данных')
			sys.exit(1)

	def GetEnrolleeId(self):
		try:
			id = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
		except AttributeError as e:
			return -1
		return id

	def SelectQuery(self):
		self.ConnnectDB()
		self.cursor = self.db.cursor()
		self.cursor.execute('SET NAMES utf8;')
		self.cursor.execute('SET CHARACTER SET utf8;')
		self.cursor.execute('SET character_set_connection=utf8;')

		self.cursor.execute("SET character_set_connection=utf8mb4")

		query = "SELECT * FROM " + groupDict[self.group]

		rows = self.cursor.execute(query)
		data = self.cursor.fetchall()

		self.tableWidget.setRowCount(rows)

		columns = self.tableWidget.columnCount()
		rows = self.tableWidget.rowCount()

		for i in range(rows):
			for j in range(columns):
				self.tableWidget.setItem(i, j, QTableWidgetItem(str(data[i][j])))

	def DeleteQuery(self):
		self.id = self.GetEnrolleeId()
		if self.id == -1:
			QMessageBox.about(self, 'Ошибка', 'Вы не выбрали строку с данными')
			return

		self.ConnnectDB()
		self.cursor = self.db.cursor()

		query = "DELETE FROM " + groupDict[self.group] +" WHERE ID = " + self.id

		self.cursor.execute(query)
		self.db.commit()
		self.SelectQuery()

class classMainMenu(QWidget, Ui_Table):

	def __init__(self):
		super().__init__()
		self.showMenu()
		self.pushBtnTableIVT()
		self.pushBtnTableIST()
		self.pushBtnExit()

	def showMenu(self):
		self.ui = uic.loadUi('UI/MainMenu.ui');
		self.ui.show()

	def pushBtnTableIVT(self):
		self.ui.btnTableIVT.clicked.connect(lambda: self.openWindowTable('ИВТ'))
	def pushBtnTableIST(self):
		self.ui.btnTableIST.clicked.connect(lambda: self.openWindowTable('ИСТ'))
	def pushBtnExit(self):
		self.ui.btnExit.clicked.connect(QtCore.QCoreApplication.quit)

	def openWindowTable(self, group):
		title = group
		self.windowTable = classTable(title)
		self.windowTable.show()

if __name__ == '__main__':
	App = QApplication(sys.argv)
	MainMenu = classMainMenu()
	sys.exit(App.exec_())