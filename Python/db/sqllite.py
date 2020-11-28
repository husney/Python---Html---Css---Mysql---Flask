import sqlite3

#conexion = sqlite3.connect("BasdeDatos")
#Si la Base de datos no existe crea el archivo DB

#cursor = conexion.cursor() #Es el puntero a la DB
#cursor.execute("CREATE TABLE PRUEBA( ID INT AUTO_INCREMENT, NOMBRE VARCHAR(20));")

#cursor.execute("INSERT INTO PRUEBA(ID, NOMBRE) VALUES (1,'Insertado')")
#conexion.commit()

#registros = [(1, "Valentina"), (2, "Sara"), (3, "Camila"), (4,"Alejandra")]

#cursor.executemany("INSERT INTO PRUEBA(ID,NOMBRE) VALUES(?,?)", registros)
#cursor.executemany(sentencia, lista)
#conexion.commit()

#for i in range(len(registros)):
   #cursor.execute("INSERT INTO PRUEBA (ID, NOMBRE) VALUES("+ str(int(i)+1) +", '" + registros[i] +"')")

#cursor.execute("SELECT * FROM PRUEBA")

#datos = cursor.fetchall()

#for registro in datos:
#   for valor in registro:
#       print(valor, end=" ")
#  print()    



#conexion = sqlite3.connect("PRODUCTOSDB")

#cursor = conexion.cursor()

#cursor.execute(""" 
#        CREATE TABLE PRODUCTOS(
#            ID INT PRIMARY KEY,
#            NOMBRE VARCHAR(20),
#            PRECIO INT
#        ) 
#""")
#
#productos = [
#    (1, "Camisa", 40000),
#    (2, "Pantalon", 80000),
#    (3, "Zapatos", 100000),
#    (4, "Reloj", 80000)
#]
#
#cursor.executemany("INSERT INTO PRODUCTOS(ID,NOMBRE,PRECIO) VALUES(?,?,?)", productos)
#
#
#cursor.execute("SELECT * FROM PRODUCTOS")
#datos = cursor.fetchall()

#for registro in datos:
#    print("ID: ", registro[0], "PRODUCTO: ", registro[1], "PRECIO: ", registro[2])


conexion = sqlite3.connect("PRODUCTOSDB")
cursor = conexion.cursor()


#productos = [
#    (1, "Camisa", 40000),
#     (2, "Pantalon", 80000),
#    (3, "Zapatos", 100000),
#    (4, "Reloj", 80000)
#]

#cursor.executemany("INSERT INTO PRODUCTOS(ID, NOMBRE, PRECIO) VALUES (?,?,?)", productos)
#conexion.commit()




#cursor.execute("SELECT * FROM PRODUCTOS WHERE ID = 1")
#datos = cursor.fetchall()

#print(datos)


#cursor.execute("UPDATE PRODUCTOS SET NOMBRE = 'CAMISA' WHERE ID = 1")
#conexion.commit()

#cursor.execute("SELECT * FROM PRODUCTOS")
#datos = cursor.fetchall()

#print(datos)


cursor.execute("DELETE FROM PRODUCTOS WHERE ID = 4")
conexion.commit()

cursor.execute("SELECT * FROM PRODUCTOS")
datos = cursor.fetchall()

print(datos)


conexion.close()

