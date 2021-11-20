import os
import psycopg2

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

# загружаем данные из csv файлов в postgresql
with psycopg2.connect(**psql_dsn) as conn, conn.cursor() as cursor:
    for table_name in tables_names:
        # Очищаем таблицу в БД, чтобы загружать данные в пустую таблицу
        cursor.execute("""TRUNCATE content.{0}""".format(table_name))
        with open('data/{0}.csv'.format(table_name), "r") as csv_file_name:
            sql = "COPY content.{0} FROM STDIN DELIMITER ',' CSV HEADER".format(table_name)
            cursor.copy_expert(sql, csv_file_name)
