from sqlite3 import Error
from connect import create_connection, database

def action(conn, sql_command):
    result = None
    cur = conn.cursor()
    try:
        cur.execute(sql_command)
        conn.commit()
        result = cur.fetchall()
        print("Request was completed successfully!")
    except Error as er:
        print(er)
    finally:
        cur.close()
    return result

if __name__ == '__main__':

    sql_pragma_foreign_key_on = """
    PRAGMA foreign_keys = ON;
    """

    with create_connection(database) as conn:
        
        print("Отримати всі завдання певного користувача:")
        select_id = action(conn, "SELECT * FROM tasks WHERE user_id=10;")
        print(select_id)

        print("-" * 150)

        print("Вибрати завдання за певним статусом:")
        select_new = action(conn, "SELECT * FROM tasks WHERE status_id=1;")
        print(select_new)

        print("-" * 150)

        print("Оновити статус конкретного завдання:")
        change_status = action(conn, "UPDATE tasks SET status_id=2 WHERE id=9;")
        print(change_status)

        print("-" * 150)

        print("Отримати список користувачів, які не мають жодного завдання:")
        select_no_task_user = action(conn, "SELECT fullname FROM users WHERE id NOT IN (SELECT user_id FROM tasks);")
        print(select_no_task_user)

        print("-" * 150)

        print("Додати нове завдання для конкретного користувача:")
        insert_task = action(conn, "INSERT INTO tasks (title, description, status_id, user_id) VALUES ('Python project', 'Make changes in Python project (PP12569)', 1, 3);")
        print(insert_task)

        print("-" * 150)

        print("Отримати всі завдання, які ще не завершено:")
        select_not_finished_task = action(conn, "SELECT * FROM tasks WHERE status_id IN(1,2);")
        print(select_not_finished_task)

        print("-" * 150)

        print("Видалити конкретне завдання:")
        delete_task = action(conn, "DELETE FROM tasks WHERE id=10;")
        print(delete_task)

        print("-" * 150)

        print("Знайти користувачів з певною електронною поштою:")
        select_email = action(conn, "SELECT email FROM users WHERE email LIKE '%@example.org%';")
        print(select_email)

        print("-" * 150)

        print("Оновити ім'я користувача:")
        change_user_name = action(conn, "UPDATE users SET fullname='Jack Sparrow' WHERE id=1;")
        print(change_user_name)

        print("-" * 150)

        print("Отримати кількість завдань для кожного статусу:")
        count_tasks_by_status = action(conn, "SELECT COUNT(status_id) as id, status_id FROM tasks GROUP BY status_id;")
        print(count_tasks_by_status)

        print("-" * 150)

        print("Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти:")
        choose_task_by_user = action(conn, "SELECT u.fullname, t.title AS task FROM users AS u JOIN tasks AS t ON t.user_id = u.id WHERE email LIKE '%@example.com%';")
        print(choose_task_by_user)

        print("-" * 150)

        print("Отримати список завдань, що не мають опису:")
        choose_task_no_description = action(conn, "SELECT title FROM tasks WHERE description=NULL;")
        print(choose_task_no_description)

        print("-" * 150)

        print("Вибрати користувачів та їхні завдання, які є у статусі 'in progress':")
        choose_user_task_in_progress = action(conn, "SELECT u.fullname, u.email, t.title AS task FROM users AS u INNER JOIN tasks AS t ON t.user_id = u.id WHERE status_id=2;")
        print(choose_user_task_in_progress)

        print("-" * 150)
        
        print("Отримати користувачів та кількість їхніх завдань:")
        select_user_task_quantity = action(conn, "SELECT u.id, u.fullname, COUNT(t.title) AS task FROM users As u LEFT JOIN tasks AS t ON t.user_id = u.id GROUP BY u.id;")
        print(select_user_task_quantity)

        print("-" * 150)