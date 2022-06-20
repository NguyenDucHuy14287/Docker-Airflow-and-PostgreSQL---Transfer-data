import psycopg2
import config


def create_tables_transactions():
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
        params = config.config_y()
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


def drop_tables_transactions():
    conn = None
    try:
        # read the connection parameters
        params = config.config_y()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        cur.execute("DROP TABLE transactions")
        # close communication with the PostgreSQL database server

        print("=>DROP table transactions y successful")

        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_transaction(creation_date, sale_value):
    sql = """INSERT INTO transactions (id, creation_date, sale_value)
             VALUES(%s, %s, %s) RETURNING id;"""
    conn = None
    id = None
    try:
        # read database configuration
        params = config.config_y()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (creation_date, sale_value))
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

    return id


def insert_list_transaction(_list):
    sql = """INSERT INTO transactions (creation_date, sale_value)
             VALUES(%s, %s);"""
    conn = None
    id = None
    try:
        # read database configuration
        params = config.config_y()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement

        for d in _list:
            print("insert data: ", d)
            cur.execute(sql, d)

        print("insert list transaction successful")

        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return id


def get_transactions():
    conn = None
    try:
        params = config.config_y()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM transactions ORDER BY id ASC")
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def get_last_id():
    conn = None
    id = 0
    try:
        params = config.config_y()
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

    return id or [0]


def truncate_transaction():
    conn = None
    try:
        params = config.config_y()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("TRUNCATE transactions RESTART IDENTITY CASCADE")
        conn.commit()
        print("=>TRUNCATE TABLE transactions SUCCESSFUL")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
