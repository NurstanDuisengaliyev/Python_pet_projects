from config import config
import psycopg2


sql = """
CREATE OR REPLACE PROCEDURE delete_user(v_opt varchar, v_var varchar)
AS
$$
BEGIN
    IF v_opt = 'name' THEN
        DELETE FROM PhoneBook WHERE contact_name = v_var;
    ELSIF v_opt = 'phone' THEN
        DELETE FROM PhoneBook WHERE contact_number = v_var;
    END IF;
END; $$

LANGUAGE plpgsql;
"""

params = config()
conn = psycopg2.connect(**params)

cursor = conn.cursor()

cursor.execute(sql)
input1 = input("name or phone?\n")
input2 = input()
cursor.execute("CALL delete_user(%s, %s)", (input1, input2))


cursor.close()
conn.commit()
conn.close()