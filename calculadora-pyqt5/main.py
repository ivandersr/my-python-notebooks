import sys
from PyQt5.QtWidgets import \
    QApplication, \
    QMainWindow, \
    QWidget, \
    QGridLayout, \
    QPushButton, \
    QLineEdit, \
    QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.error_text = 'Expressão inválida'
        self.setWindowTitle('Calculadora da Galera')
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background: #fff; color: #000; font-size: 32px}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.add_btn(QPushButton('7'), 1, 0, 1, 1)
        self.add_btn(QPushButton('8'), 1, 1, 1, 1)
        self.add_btn(QPushButton('9'), 1, 2, 1, 1)
        self.add_btn(QPushButton('+'), 1, 3, 1, 1)
        self.add_btn(
            QPushButton('C'), 1, 4, 1, 1,
            lambda: self.display.setText(''),
            'background: #d5580d;'
            'font-weight: bold;'
            'color: #fff'
        )

        self.add_btn(QPushButton('4'), 2, 0, 1, 1)
        self.add_btn(QPushButton('5'), 2, 1, 1, 1)
        self.add_btn(QPushButton('6'), 2, 2, 1, 1)
        self.add_btn(QPushButton('-'), 2, 3, 1, 1)
        self.add_btn(
            QPushButton('<-'), 2, 4, 1, 1,
            lambda: self.display.setText(self.display.text()[:-1]),
            'background: #d49900;'
            'font-weight: bold;'
            'color: #fff'
        )

        self.add_btn(QPushButton('1'), 3, 0, 1, 1)
        self.add_btn(QPushButton('2'), 3, 1, 1, 1)
        self.add_btn(QPushButton('3'), 3, 2, 1, 1)
        self.add_btn(QPushButton('/'), 3, 3, 1, 1)
        self.add_btn(
            QPushButton('='), 3, 4, 2, 1,
            self.eval_eq,
            'background: #239955;'
            'font-weight: bold;'
            'color: #fff'
        )

        self.add_btn(QPushButton('0'), 4, 0, 1, 2)
        self.add_btn(QPushButton('.'), 4, 2, 1, 1)
        self.add_btn(QPushButton('*'), 4, 3, 1, 1)

        self.setCentralWidget(self.cw)

    def add_btn(self, btn, row, col, rowspan, colspan, funcao=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)
        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )
            )
        else:
            btn.clicked.connect(funcao)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def eval_eq(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as err:
            self.display.setText(self.error_text)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
