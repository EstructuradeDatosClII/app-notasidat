from util.ConexionBd import ConexionBd

class CursoDao:
    
    def __init__(self) -> None:
        self.conexion = ConexionBd().getConexionBD()
    
    def listarCursos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT idcurso,nomcurso,credito FROM CURSO ORDER BY idcurso DESC"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def insertarCurso(self, curso):
        exec = self.conexion.cursor()
        sql = "INSERT INTO curso VALUES('{}','{}','{}')".format(
            curso.codcurso, curso.nomcurso, curso.credcurso
        )
        exec.execute(sql)
        self.conexion.commit()
        exec.close()