import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="emaildb"
)

mycursor = mydb.cursor()

#CONSTANTS pel resultat de les fucions
NOTROBAT = "NOTROBAT"
AFEGIT = "AFEGIT"
MODIFICAT = "MODIFICAT"
JAEXISTEIX = "JAEXISTEIX"

def sqlgetmail(nombre):
    sql = "SELECT correu FROM usuarios WHERE NOM = %s"
    mycursor.execute(sql, (nombre,))
    myresult = mycursor.fetchall()
    for x in myresult:
        return x[0]
    return NOTROBAT

def sqladdUser(nombre,correo,modif=False):
    oldcorreu = sqlgetmail(nombre)
    sqlinsert = "INSERT INTO usuarios (NOM, correu) VALUES (%s, %s)"
    sqlupdate = "UPDATE usuarios SET correu = (%s) WHERE nom = (%s)"
    val = (nombre, correo)
    if oldcorreu == NOTROBAT:
        mycursor.execute(sqlinsert, val)
        return AFEGIT
    elif (oldcorreu != correo and modif):
        mycursor.execute(sqlupdate, val)
        return MODIFICAT
    mydb.commit()
