import psycopg2
from config import config

def update_user(username, lvl, score, body_pos, direction):  # username, lvl, score, body_pos, direction
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        sql = """
            UPDATE user_score
            SET lvl = %s, score = %s, snake_pos = %s, direction = %s
            WHERE username = %s
        """
        cur.execute(sql, (lvl, score, body_pos, direction, username))
        conn.commit()
        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.close()
