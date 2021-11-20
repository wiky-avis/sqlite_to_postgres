import io
import os
import sqlite3
import psycopg2
import subprocess

psql_dsn = {
 'dbname': 'moviesdb',
 'user': 'userdb',
 'password': 'password',
 'host': '127.0.0.1',
 'port': 5432
}

tables_names = ["film_work", "genre", "genre_film_work", "person", "person_film_work"]

# создаем папку для csv файлов
os.system("mkdir data")
# сохраняем данные из таблиц из sqlite в csv файлы c соответствующими названиями, в папку data
for table_name in tables_names:
    os.system(
     "sqlite3 -header -csv db.sqlite 'SELECT DISTINCT * FROM {0};' > data/{1}.csv".format(table_name, table_name)
    )

