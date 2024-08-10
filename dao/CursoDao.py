from util.ConexionBd import ConexionBd

class CursoDao:
    
    def __init__(self) -> None:
        self.conexion = ConexionBd().getConexionBD()
    
    def listarCursos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT idcurso,nomcurso,credito FROM CURSO ORDER BY idcurso DESC"
        cursor.execute(sql)
        return cursor.fetchall()

    def obtenerCurso(self, idcurso):
        cursor = self.conexion.cursor()
        sql = "SELECT idcurso,nomcurso,credito FROM CURSO WHERE idcurso = '{}'".format(
            idcurso)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarCurso(self, curso):
        exec = self.conexion.cursor()
        sql = "INSERT INTO curso VALUES('{}','{}','{}')".format(
            curso.codcurso, curso.nomcurso, curso.credcurso
        )
        exec.execute(sql)
        self.conexion.commit()
        exec.close()
        
    def actualizarCurso(self, curso):
        exec = self.conexion.cursor()
        sql = "UPDATE CURSO SET nomcurso='{}', credito='{}' WHERE idcurso='{}'".format(
            curso.nomcurso, curso.credcurso, curso.codcurso)
        exec.execute(sql)
        self.conexion.commit()
        exec.close()