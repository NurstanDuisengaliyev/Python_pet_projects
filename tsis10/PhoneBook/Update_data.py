import psycopg2
from config import config

def update_data(number, new_name, new_number):
    sql = """
        UPDATE PhoneBook
        SET contact_number = %s, contact_name=%s
        WHERE contact_number = %s
    """
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (new_number, new_name, number))
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    update_data(number="77071436710", new_number="87071436711", new_name="Sagatbek")