import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
import sqlite3 as db
from add_edit_ui import Ui_Form as EditForm
from main_ui import Ui_Form as MainForm


class EditWindow(QWidget, EditForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.push)

    def push(self):
        try:
            v1 = int(self.in1.text()) if self.in1.text() else None
            v2 = self.in2.text()
            v3 = self.in3.text()
            v4 = self.in4.text()
            v5 = self.in5.text()
            v6 = int(self.in6.text())
            v7 = int(self.in7.text())
            con = db.connect('data/coffee.sqlite')
            cur = con.cursor()
            if v1:
                cur.execute("""UPDATE coffee SET variety = '{}', roasting = '{}', type = '{}', taste = '{}',
                price = {}, volume = {} WHERE id = {}""".format(v2, v3, v4, v5, v6, v7, v1))
            else:
                cur.execute("""INSERT INTO coffee (variety, roasting, type, taste, price, volume) VALUES
                ('{}', '{}', '{}', '{}', {}, {})""".format(v2, v3, v4, v5, v6, v7))
            con.commit()
            self.close()
            global ex
            ex.start()
        except Exception:
            self.out.setText('Данные введены не правильно')


class Example(QWidget, MainForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start()
        self.editbtn.clicked.connect(self.push)

    def start(self):
        con = db.connect('data/coffee.sqlite')
        cur = con.cursor()
        res = cur.execute("""SELECT * FROM coffee""").fetchall()
        self.draw(res)

    def draw(self, data):
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(['ID', 'Сорт', 'Обжарка', 'Тип', 'Вкус', 'Цена', 'Объем'])
        self.table.setRowCount(0)
        for i, row in enumerate(data):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                item = QTableWidgetItem(str(elem))
                item.setFlags(Qt.ItemIsEnabled)
                self.table.setItem(i, j, item)
        self.table.resizeColumnsToContents()

    def push(self):
        self.w = EditWindow()
        self.w.show()


app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec())
