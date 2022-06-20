import psycopg2
import config


def create_tables_transactions():
    commands = """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE transactions (
               id SERIAL PRIMARY KEY,
               creation_date varchar NOT NULL,
               sale_value bigint NOT NULL
                )
        """,
    )
    conn = None
    try:
        # read the connection parameters
        params = config.config_x()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server

        print("=>table transactions in database y successful")

        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_transaction(creation_date, sale_value):
    sql = """INSERT INTO transactions (creation_date, sale_value)
             VALUES(%s, %s) RETURNING id;"""
    conn = None
    id = None
    try:
        # read database configuration
        params = config.config_x()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (creation_date, sale_value))
        conn.commit
        # get the generated id back
        id = cur.fetchone()[0]

        print("=> insert successful, id: ", id)

        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id or 0


def get_transactions(condition=None):
    conn = None
    _list = []
    try:
        params = config.config_x()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        if condition is None:
            cur.execute("SELECT * FROM transactions ORDER BY id ASC")
        else:
            cur.execute("SELECT creation_date, sale_value FROM transactions " + condition + " ORDER BY id ASC")

        print("The number of parts: ", cur.rowcount)

        if condition is None:
            row = cur.fetchone()
            while row is not None:
                print(row)
                row = cur.fetchone()
        else:
            _list = cur.fetchall()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return _list


def get_last_id():
    conn = None
    id = 0
    try:
        params = config.config_x()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT id FROM transactions ORDER BY id DESC")
        id = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id
