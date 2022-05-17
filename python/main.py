from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_calculadora import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        """ Conectando Botones """
        self.ui.btncero.clicked.connect(self.btn_cero)
        self.ui.btnuno.clicked.connect(self.btn_uno)
        self.ui.btndos.clicked.connect(self.btn_dos)
        self.ui.btntres.clicked.connect(self.btn_tres)
        self.ui.btncuatro.clicked.connect(self.btn_cuatro)
        self.ui.btncinco.clicked.connect(self.btn_cinco)
        self.ui.btnseis.clicked.connect(self.btn_seis)
        self.ui.btnsiete.clicked.connect(self.btn_siete)
        self.ui.btnocho.clicked.connect(self.btn_ocho)
        self.ui.btnnueve.clicked.connect(self.btn_nuevo)
        self.ui.btnpunto.clicked.connect(self.btn_punto)
        self.ui.btnsuma.clicked.connect(self.btn_suma)
        self.ui.btnresta.clicked.connect(self.btn_resta)
        self.ui.btndiv.clicked.connect(self.btn_div)
        self.ui.btnmulti.clicked.connect(self.btn_multi)
        self.ui.btnenter.clicked.connect(self.btn_enter)
        self.ui.btnclear.clicked.connect(self.btn_clear)
        """ Fin conecion de Botones"""
    

    """Construccion de Botones Funciones"""
    @Slot()
    def btn_cero(self):
        entrada = self.ui.txtmostrar.text()
        entrada += "0"
        self.ui.txtmostrar.setText(entrada)
        
    @Slot()
    def btn_uno(self):
        entrada = self.ui.txtmostrar.text()
        entrada += "1"
        self.ui.txtmostrar.setText(entrada)
    @Slot()
    def btn_dos(self):
        entrada = self.ui.txtmostrar.text()
        entrada += "2"
        self.ui.txtmostrar.setText(entrada)
    @Slot()
    def btn_tres(self):
        entrada = self.ui.txtmostrar.text()
        entrada += "3"
        self.ui.txtmostrar.setText(entrada)
    @Slot()
    def btn_cuatro(self):
        entrada = self.ui.txtmostrar.text()
        entrada += "4"
        self.ui.txtmostrar.setText(entrada)
    @Slot()
    def btn_cinco(self):
        entrada = self.ui.txtmostrar.text()
        entrada += "5"
        self.ui.txtmostrar.setText(entrada)
    @Slot()
    def btn_seis(self):
        entrada = self.ui.txtmostrar.text()
        entrada += "6"
        self.ui.txtmostrar.setText(entrada)
    @Slot()
    def btn_siete(self):
        entrada = self.ui.txtmostrar.text()
        entrada += "7"
        self.ui.txtmostrar.setText(entrada)
    @Slot()
    def btn_ocho(self):
        entrada = self.ui.txtmostrar.text()
        entrada += "8"
        self.ui.txtmostrar.setText(entrada)
    @Slot()
    def btn_nuevo(self):
        entrada = self.ui.txtmostrar.text()
        entrada += "9"
        self.ui.txtmostrar.setText(entrada)
    @Slot()
    def btn_punto(self):
        entrada = self.ui.txtmostrar.text()
        entrada += "."
        self.ui.txtmostrar.setText(entrada)
    @Slot()
    def btn_suma(self):
        entrada = self.ui.txtmostrar.text()
        entrada += "+"
        self.ui.txtmostrar.setText(entrada)
    @Slot()
    def btn_multi(self):
       entrada = self.ui.txtmostrar.text()
       entrada += "*"
       self.ui.txtmostrar.setText(entrada)
    @Slot()
    def btn_div(self):
        entrada = self.ui.txtmostrar.text()
        entrada += "/"
        self.ui.txtmostrar.setText(entrada)
    @Slot()
    def btn_resta(self):
        entrada = self.ui.txtmostrar.text()
        entrada += "-"
        self.ui.txtmostrar.setText(entrada)
    
    
    @Slot()
    def btn_enter(self):
        entrada = self.ui.txtmostrar.text()
        try:
            entrada = eval(entrada)
            self.ui.txtmostrar.setText(str(entrada))
        except:
            self.ui.txtmostrar.setText("ERROR!!")

    @Slot()
    def btn_clear(self):
        self.ui.txtmostrar.clear()

    """Fin de conexiones de botones"""