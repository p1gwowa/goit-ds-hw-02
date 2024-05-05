from sqlite3 import Error
from connect import create_connection, database

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as er:
        print(er)

def drop_table(conn, drop_table_sql):
    try:
        c = conn.cursor()
        c.execute(drop_table_sql)
        conn.commit()
    except Error as er:
        print(er)

if __name__ == '__main__':

    sql_drop_users_table = """
    DROP TABLE IF EXISTS users;
    """

    sql_create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(100),
    email VARCHAR(100) UNIQUE
    );
    """

    sql_drop_status_table = """
    DROP TABLE IF EXISTS status;
    """
    
    sql_create_status_table = """
    CREATE TABLE IF NOT EXISTS status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    CONSTRAINT status_name_un UNIQUE (name)
    );
    """

    sql_drop_tasks_table = """
    DROP TABLE IF EXISTS tasks;
    """

    sql_create_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100),
    description TEXT,
    status_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (status_id) REFERENCES status (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
    FOREIGN KEY (user_id) REFERENCES users (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
    );
    """

    with create_connection(database) as conn:

        if conn is not None:

            drop_table(conn, sql_drop_users_table)
            create_table(conn, sql_create_users_table)

            drop_table(conn, sql_drop_status_table)
            create_table(conn, sql_create_status_table)

            drop_table(conn, sql_drop_tasks_table)
            create_table(conn, sql_create_tasks_table)

        else:
            print("Error! Can not create the database connection.")

