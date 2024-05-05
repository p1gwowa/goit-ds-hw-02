from sqlite3 import Error
from connect import create_connection, database
from generate_data import user_data, task_data

def create_users(conn, user):
    sql = """
    INSERT INTO users(fullname, email) VALUES(?, ?);
    """
    cur = conn.cursor()
    try:
        cur.executemany(sql, user)
        conn.commit()
    except Error as er:
        print(er)
    finally:
        cur.close()
    
    return cur.lastrowid

def create_status(conn, stat):
    sql = """
    INSERT INTO status(name) VALUES(?);
    """
    cur = conn.cursor()
    try:
        cur.executemany(sql, stat)
        conn.commit()
    except Error as er:
        print(er)
    finally:
        cur.close()

    return cur.lastrowid

def create_task(conn, task):
    sql = """
    INSERT INTO tasks(title, description, status_id, user_id) VALUES(?, ?, ?, ?);
    """
    cur = conn.cursor()
    try:
        cur.executemany(sql, task)
        conn.commit()
    except Error as er:
        print(er)
    finally:
        cur.close()

    return cur.lastrowid

if __name__ == '__main__':

    with create_connection(database) as conn:

        users_id = create_users(conn, user_data)

        status_data = [('new',), ('in progress',), ('completed',)]
        status_id = create_status(conn, status_data)

        task_id = create_task(conn, task_data)






