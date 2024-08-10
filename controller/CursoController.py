import sys
from PyQt5 import QtWidgets, uic
from dao.CursoDao import CursoDao
from PyQt5.QtWidgets import QTableWidgetItem
from model.Curso import Curso

class CursoController:
    
    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frmcurso.ui")
        self.ventana.tblcursos.setColumnWidth(0, 75)
        self.ventana.tblcursos.setColumnWidth(1, 280)
        self.ventana.tblcursos.setColumnWidth(2, 75)
        self.ventana.btnnuevo.clicked.connect(self.onClick_BtnNuevo)
        self.ventana.btnguardar.clicked.connect(self.onClick_BtnGuardar)
        self.ventana.tblcursos.cellClicked.connect(self.onCellClick_TblCursos)
        self.cursoDao = CursoDao()
        self.listarCursos()
        self.ventana.show()        
        app.exec()
        
    def onClick_BtnGuardar(self):
        idcurso = self.ventana.txtcodigo.text()
        nomcurso = self.ventana.txtnombre.text()
        credcurso = self.ventana.txtcredito.text()
        nuevoCurso = Curso(idcurso, nomcurso, credcurso)
        if self.ventana.txtcodigo.isEnabled():
            self.cursoDao.insertarCurso(nuevoCurso)
        else:
            self.cursoDao.actualizarCurso(nuevoCurso)
        self.listarCursos()
    
    def onClick_BtnNuevo(self):
        self.ventana.txtcodigo.setText("")
        self.ventana.txtcodigo.setEnabled(True)
        self.ventana.txtnombre.setText("")
        self.ventana.txtcredito.setText("")
        
    def onCellClick_TblCursos(self, fila):
        idcurso = self.ventana.tblcursos.item(fila, 0).text()
        self.ventana.txtcodigo.setText(idcurso)
        self.ventana.txtcodigo.setEnabled(False)
        objCurso = self.cursoDao.obtenerCurso(idcurso)
        self.ventana.txtnombre.setText(objCurso[1])
        self.ventana.txtcredito.setText(str(objCurso[2]))
    
    
    def listarCursos(self):
        listaCurso = self.cursoDao.listarCursos()
        cantidad = len(listaCurso)
        self.ventana.tblcursos.setRowCount(cantidad)
        fila = 0
        for objCurso in listaCurso:
            self.ventana.tblcursos.setItem(fila, 0, 
                                           QTableWidgetItem(objCurso[0]))
            self.ventana.tblcursos.setItem(fila, 1, 
                                           QTableWidgetItem(objCurso[1]))
            self.ventana.tblcursos.setItem(fila, 2, 
                                           QTableWidgetItem(str(objCurso[2])))
            fila += 1