import psycopg2
from config import config

def get_by_name(name):
    """ query data from the PhoneBook table """

    sql = """
        SELECT contact_name, contact_number FROM PhoneBook WHERE contact_name = %s
        ORDER BY contact_number ASC
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (name,))
        print("The number of contacts with such name: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def get_by_number(number):
    """ query data from the PhoneBook table """
    conn = None
    sql = """
            SELECT contact_name, contact_number FROM PhoneBook WHERE contact_number = %s
            ORDER BY LENGTH(contact_name)
        """

    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (number,))
        print("The person with such contact number")
        row = cur.fetchone()
        print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    get_by_name("Aidar")
    get_by_number("230332493")
