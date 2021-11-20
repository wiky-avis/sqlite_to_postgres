# sqlite_to_postgres
Перенос данных из SQLite в Postgres


Запустить контейнер с Postgresql и спроектировать БД для переноса [контейнер и инструкция тут](https://github.com/wiky-avis/psql-container.git).

Установите виртуальное окружение

    `python -m venv venv`

и активируйте его:
    
    `source venv/bin/activate`

Установите зависимости:

    `pip install -r requirements.txt`

Запустите скрипт:

    `python sql_to_psql.py`


После запуска скрипт автоматически создаст папку "data" и выгрузит в нее данные из базы SQLite в csv файлы, затем загрузит в базу Postgresql. В комплекте тестовая база SQLite.
