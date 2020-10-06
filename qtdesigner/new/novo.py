import sys
from new.design import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class Redimensionator(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.open_img)
        self.btnRedimensionar.clicked.connect(self.redimensionar)
        self.btnSalvar.clicked.connect(self.salvar)
        self.original_img = ''
        self.nova_imagem = ''

    def open_img(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir imagem',
            r'E:\Downloads'
        )
        self.inputAbrirArquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.labelImg.setPixmap(self.original_img)
        self.inputLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))

    def redimensionar(self):
        largura = int(self.inputLargura.text())
        self.nova_imagem = self.original_img.scaledToWidth(largura)
        self.labelImg.setPixmap(self.nova_imagem)
        self.inputLargura.setText(str(self.nova_imagem.width()))
        self.inputAltura.setText(str(self.nova_imagem.height()))

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar imagem',
            r'E:\Downloads'
        )
        self.nova_imagem.save(imagem, 'png')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    redimensionator = Redimensionator()
    redimensionator.show()
    qt.exec_()
