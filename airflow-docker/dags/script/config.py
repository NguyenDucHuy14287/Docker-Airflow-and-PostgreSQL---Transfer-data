from configparser import ConfigParser


def config_x():
    return {
        "host": "postgres_x",
        "port": "5432",
        "database": "airflow",
        "user": "airflow",
        "password": "airflow",
    }

def config_y():
    return {
        "host": "postgres_y",
        "port": "5432",
        "database": "airflowy",
        "user": "airflowy",
        "password": "airflowy",
    }
