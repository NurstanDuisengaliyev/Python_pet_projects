from config import config
import psycopg2

contact_name = input()
contact_number = input()

sql = '''
    CREATE OR REPLACE PROCEDURE insert_user(name varchar, number varchar)
    AS
    $$
    BEGIN
        IF EXISTS (SELECT FROM PhoneBook WHERE contact_name = name) THEN
            UPDATE PhoneBook SET contact_number = number WHERE contact_name = name;
        ELSE
            INSERT INTO PhoneBook (contact_number, contact_name) VALUES(number, name);
        END IF;
    END; $$
    
    LANGUAGE plpgsql;
'''


params = config()
conn = psycopg2.connect(**params)

cursor = conn.cursor()

cursor.execute(sql)
cursor.execute('CALL insert_user(%s, %s)', (contact_name, contact_number))
cursor.close()
conn.commit()
conn.close()