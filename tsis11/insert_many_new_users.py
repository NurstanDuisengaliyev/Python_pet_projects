from config import config
import psycopg2

sql = '''
CREATE OR REPLACE PROCEDURE insert_new_users(VARIADIC v_vars varchar[])
AS
$$
BEGIN
    FOR i in 1..array_upper(v_vars, 1) by 2 LOOP
        IF v_vars[i+1] ~ '^(\+7|8)?\d{10}' THEN
            INSERT INTO PhoneBook (contact_number, contact_name) VALUES(v_vars[i+1], v_vars[i]);
        ELSE
            RAISE NOTICE 'SORRY, THE NUMBER % IS INCORRECT', v_vars[i+1];
        END IF;
    END LOOP;
END;
$$
LANGUAGE plpgsql;
'''


params = config()

conn = psycopg2.connect(**params)

cursor = conn.cursor()

cursor.execute(sql)

sql = """
    CALL insert_new_users('Baibory', '77432346587', 'Nurs', '+87071833143', 'Dimash', '234313132', 'sdfk', 'sdfl');
"""

cursor.execute(sql)

incorrect_phones_list = cursor.fetchone()[0]
print(f"Incorrect phone numbers: {incorrect_phones_list}")

cursor.close()
conn.commit()
conn.close()