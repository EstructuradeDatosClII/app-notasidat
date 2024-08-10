import sys
from PyQt5 import QtWidgets, uic
from dao.CursoDao import CursoDao
from PyQt5.QtWidgets import QTableWidgetItem
from model.Curso import Curso

class CursoController:
    
    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frmcurso.ui")
        self.ventana.show()
        app.exec()