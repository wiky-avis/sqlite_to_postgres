# sqlite_to_postgres
Перенос данных из SQLite в Postgres


Запустить контейнер с Postgresql и спроектировать БД для переноса [контейнер и инструкция тут](https://github.com/wiky-avis/psql-container.git).

Установите виртуальное окружение и активируйте его:
    `python -m venv venv`

    
    `source venv/bin/activate`

Установите зависимости:

    `pip install -r requirements.txt`

Запустите скрипт:

    `python sql_to_psql.py`


После запуска скрипт автоматически создаст папку "data" и выгрузит данные из базы SQLite в csv файлы, затем загрузит в базу Postgresql. В комплекте тестовая база SQLite.
