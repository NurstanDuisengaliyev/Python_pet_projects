import psycopg2
from config import config

def create_table():
    command1 = """
        CREATE TABLE users (
            username VARCHAR(255) PRIMARY KEY NOT NULL 
        )
    """
    command2 = """
        CREATE TABLE user_score (
            username VARCHAR(255) NOT NULL PRIMARY KEY,
            lvl INTEGER, 
            score INTEGER, 
            snake_pos VARCHAR(255) NOT NULL, 
            direction INTEGER,
            FOREIGN KEY (username)
                REFERENCES users (username)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
    """
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table
        cur.execute(command1)
        cur.execute(command2)
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
    create_table()