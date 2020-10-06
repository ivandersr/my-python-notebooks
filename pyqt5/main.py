import sys
from \
    PyQt5.QtWidgets \
    import \
    QMainWindow, \
    QApplication, \
    QPushButton, \
    QWidget, \
    QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.btn = QPushButton('Clique aqui')
        self.btn.setStyleSheet('font-size: 16px')

        self.btn.clicked.connect(self.btn_click)

        self.grid.addWidget(self.btn, 0, 0, 1, 1)
        self.setCentralWidget(self.cw)

    @staticmethod
    def btn_click():
        print('Botão clicado')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
