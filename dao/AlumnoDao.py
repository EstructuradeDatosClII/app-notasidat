from util.ConexionBd import ConexionBd

class AlumnoDao:
    
    def __init__(self) -> None:
        self.conexion = ConexionBd().getConexionBD()

    def listarAlumnos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT a.idalumno, a.nomalumno, a.apealumno, "
        sql += "e.nomesp FROM alumno a INNER JOIN especialidad e "
        sql +=" ON a.IdEsp = e.IdEsp ORDER BY a.idalumno DESC"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def obtenerAlumno(self, idalumno):
        cursor = self.conexion.cursor()
        sql = "SELECT a.idalumno, a.nomalumno, a.apealumno, "
        sql += "e.nomesp, a.proce FROM alumno a INNER JOIN especialidad e "
        sql +=" ON a.IdEsp = e.IdEsp WHERE a.idalumno='{}'".format(idalumno)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarAlumno(self, alumno):
        exec = self.conexion.cursor()
        sql = "INSERT INTO alumno (idalumno,nomalumno,apealumno,idesp,proce) VALUES('{}','{}','{}','{}','{}')".format(
            alumno.codalumno, alumno.nomalumno, alumno.apealumno,
            alumno.idespecialidad, alumno.procedencia
        )
        exec.execute(sql)
        self.conexion.commit()
        exec.close()
    def actualizarAlumno(self, alumno):
        exec = self.conexion.cursor()
        sql = "UPDATE alumno SET nomalumno='{}', apealumno='{}',idesp='{}',proce='{}' WHERE idalumno='{}'".format(
            alumno.nomalumno, alumno.apealumno,
            alumno.idespecialidad, alumno.procedencia,
            alumno.codalumno)
        exec.execute(sql)
        self.conexion.commit()
        exec.close()