import mysql.connector 

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost", 
            user="root",       
            password="your_password", 
            database="your_database"  
        )
        print("Lidhja me bazën e të dhënave u krye me sukses!")
        return connection
    except mysql.connector.Error as e:
        print(f"Gabim gjatë lidhjes: {e}")
        return None

def insert_record(connection, table, data):
    cursor = connection.cursor()
    
    values = tuple(data)
    try:
        cursor.execute(query, values)
        connection.commit()
        print(f"Regjistri u shtua me sukses në tabelën {table}.")
    except mysql.connector.Error as e:
        print(f"Gabim gjatë shtimit të regjistrit: {e}")
    finally:
        cursor.close()