import pymysql

database = pymysql.connect("qabu343.areaife.com","qabu343","A150917y","qabu343")
cur = database.cursor()

def subir():
    insert = "INSERT INTO `Información Mensual` (codigoAgencia, fechaEnvio, personaAtendida, personaDesempleo, personaDificultadInsercion, ofertaTrabajoCaptada, ofertaTrabajoCubierta, puestoTrabajoCaptado, puestoTrabajoCubierto, contratoSuscrito, contratoIndefinido, personaNueva, personaOferta, personaColocada) VALUES ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14');"
    cur.execute(insert)

def mostrar():
    cur.execute("SELECT * FROM `Información Mensual`")
    myresult = cur.fetchall()
    for x in myresult:
      print(x)    


subir()
mostrar()

database.commit()
