import psycopg2
from config import config
import csv

def stand_number(number):
    standn = ""
    for c in number:
        if c.isdigit():
            standn += c

    return standn

def insert_csv(file_path):

    sql = """
        INSERT INTO PhoneBook(contact_number, contact_name)
        VALUES(%s, %s)
    """

    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            for row in reader:
                #print(row)
                cur.execute(sql, (stand_number(row[1]), row[0]))

        # commit changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    insert_csv(("/Users/nurstanduisengaliyev/Documents/Python/pp2-22B031491/tsis10/PhoneBook/CSV_FILE.csv"))