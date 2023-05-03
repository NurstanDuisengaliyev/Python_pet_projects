import psycopg2
from config import config
import csv

def stand_number(number):
    standn = ""
    for c in number:
        if c.isdigit():
            standn += c

    return standn

def insert_console(name, number):

    sql = """
        INSERT INTO PhoneBook(contact_number, contact_name)
        VALUES(%s, %s)
    """

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute(sql, (stand_number(number), name))
        # commit changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    input = input("Please, write name and contact number\n")
    name, number = input.split()
    insert_console(name, number)