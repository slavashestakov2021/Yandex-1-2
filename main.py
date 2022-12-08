import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
import sqlite3 as db


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.start()

    def start(self):
        con = db.connect('coffee.sqlite')
        cur = con.cursor()
        res = cur.execute("""SELECT * FROM coffee""").fetchall()
        con = db.connect('coffee.sqlite')
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
