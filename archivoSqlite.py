import sqlite3

def crearTabla(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS alumno(
            alumno_id INTEGER PRIMARY KEY AUTOINCREMENT,
            alumno_nombre VARCHAR(20) NOT NULL,
            alumno_apellidopat varchar(20) NOT NULL,
            alumno_apellidomat varchar(20) NOT NULL,
            alumno_grupo varchar(10)
               );''');
    print("tabla Alumno creada")

def ingresaAlumno(cursor, nombre, apellidoPaterno, apellidoMaterno, grupo):
    insertaAlumno="INSERT INTO alumno(alumno_nombre, alumno_apellidopat, alumno_apellidomat, alumno_grupo) VALUES('"+nombre+"','"+apellidoPaterno+"','"+apellidoMaterno+"','"+grupo+"');"
    cursor.execute(insertaAlumno)
    bd.commit()
    print("se inserto el alumno")
    enlistaAlumnos(cursor)

def borraAlumno(cursor,idAlumno):
    borrarAlumno="DELETE FROM alumno WHERE alumno_id="+idAlumno+";"
    cursor.execute(borrarAlumno)
    bd.commit()
    print("se elimino el alumno")
    enlistaAlumnos(cursor)

def enlistaAlumnos(cursor):
    selectAlumnos="SELECT * FROM alumno"
    cursor.execute(selectAlumnos)

    for campo in cursor:
        print("\nID: ",campo[0])
        print("NOMBRE: "+campo[1])
        print("APELLIDO PATERNO: ",campo[2])
        print("APELLIDO MATERNO: ",campo[3])
        print("GRUPO: ",campo[4])


bd = sqlite3.connect("base_de_datos.db")
#bd = sqlite3.connect(":memory:")
print("Base de datos abierta")

cursor= bd.cursor()

crearTabla(cursor)
enlistaAlumnos(cursor)

while True:
    opcion=int(input("¿Desea 1)insertar un alumno o 2) eliminar un alumno? "))

    if opcion == 1:
        nombre = input("Nombre: ")
        apellidoPaterno = input("Apellido Paterno: ")
        apellidoMaterno = input("Apellido Materno: ")
        grupo = input("Grupo: ")
        ingresaAlumno(cursor, nombre, apellidoPaterno, apellidoMaterno, grupo)
    elif opcion == 2:
        idAlumno = input("Ingresa el id del alumno a eliminar: ")
        borraAlumno(cursor,idAlumno)
    
bd.close()