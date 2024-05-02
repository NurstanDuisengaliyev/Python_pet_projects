import psycopg2
from config import config

def get_user(username, WIDTH, HEIGHT):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", (username, ))
        row = cur.fetchone()
        if row is None:  # We should insert new one
            sql = "INSERT INTO users(username) VALUES(%s)"
            cur.execute(sql, (username, ))
            sql = "INSERT INTO user_score(username, lvl, score, snake_pos, direction) VALUES(%s, %s, %s, %s, %s)"
            body_pos = f"{WIDTH // 30 // 2}, {HEIGHT // 30 // 2}; {WIDTH // 30 // 2 + 1}, {HEIGHT // 30 // 2}"
            cur.execute(sql, (username, 0, 0, body_pos, 0))
            conn.commit()
            cur.close()
            conn.close()
            return [username, 0, 0, body_pos, 0]
        else:  # It exists just SELECT it.
            sql = """SELECT * FROM user_score WHERE username = %s"""
            cur.execute(sql, (username, ))
            row = cur.fetchone()
            conn.commit()
            cur.close()
            conn.close()
            return [row[0], row[1], row[2], row[3], row[4]]
            # username, lvl, score, body_pos, direction



    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
