import sqlite3


def search(search):
    connection = sqlite3.connect("fl_tech_plates.db")
    cursor = connection.cursor()

    sql_command = "SELECT * FROM plates WHERE plate_number LIKE ?"
    found_plate = cursor.execute(sql_command, (''.join(("%",search.lower(),"%")),))
    
    re = list(found_plate)
    connection.close()
    return re