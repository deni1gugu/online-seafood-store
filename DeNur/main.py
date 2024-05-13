import psycopg2
from config import host, user, password, db_name

connection = None

try:
    # connect to exist database 
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )


    with connection.cursor() as cursor:
        pass

        rows = cursor.fetchall()
        decoded_rows = [[cell.decode('utf-8') if isinstance(cell, bytes) else cell for cell in row] for row in rows]
        
        for row in decoded_rows:
           print(row)

except Exception as _ex:
    print("(INFO) Error while working with PostgresSQL", _ex)
finally:
    if connection:
        connection.close()
        print("(INFO) PostgresSQL connection closed")