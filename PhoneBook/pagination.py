from config import config
import psycopg2


sql = '''
CREATE OR REPLACE FUNCTION pagination(l integer, r integer)
  RETURNS TABLE(contact_name VARCHAR, contact_number VARCHAR) AS
$$
BEGIN
    RETURN QUERY

    SELECT *
    FROM PhoneBook
    LIMIT r OFFSET l-1;

END; $$

LANGUAGE plpgsql;
'''

params = config()
conn = psycopg2.connect(**params)

cursor = conn.cursor()

cursor.execute(sql)
l, r = 2, 4  # from 2 to 4th ones
cursor.execute(f"SELECT pagination({l}, {r})")
records = cursor.fetchall()

print(records)

cursor.close()
conn.commit()
conn.close()