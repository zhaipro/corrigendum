rmdir /S /Q main\migrations
rm db.sqlite3
manage.py makemigrations main
manage.py migrate
manage.py createsuperuser --username admin --email xin_soft@foxmail.com
manage.py runserver