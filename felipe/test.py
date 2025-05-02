import mysql.connector
import os

db_config = {
    'user': '2QjxoUpy7qAaDCC.root',
    'password': 'GcwNjgJaCDySR46p',
    'host': 'gateway01.us-east-1.prod.aws.tidbcloud.com',
    'port': '4000',
    'database':'test'
}

#ejectutar concetarse a la bd
try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    #ejecutar consulta
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    print("coneccion exitosa",result)

except mysql.connector.Error as err:
        print("Error al conectarse a la BD", err)
    
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("coneccion cerrada")