from PyQt5 import QtWidgets, uic
from dao.AlumnoDao import AlumnoDao
from PyQt5.QtWidgets import QTableWidgetItem
from model.Alumno import Alumno

class AlumnoController:
    
    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frmalumno.ui")
        self.ventana.show()
        app.exec()
        
        