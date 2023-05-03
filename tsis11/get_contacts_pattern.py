from config import config
import psycopg2


pattern = input()


sql = """
    CREATE OR REPLACE FUNCTION get_contacts_pattern(pattern text)
    RETURNS SETOF PhoneBook AS 
    $$
    BEGIN
        RETURN QUERY SELECT * FROM PhoneBook WHERE contact_name LIKE '%' || pattern || '%'
        OR contact_number LIKE '%' || pattern || '%';
    END;
$$ LANGUAGE plpgsql;
"""


params = config()
conn = psycopg2.connect(**params)
cursor = conn.cursor()


cursor.execute(sql)
cursor.execute('SELECT get_contacts_pattern (%s)',(f'{pattern}',))
print(cursor.fetchall())
cursor.close()
conn.commit()
conn.close()