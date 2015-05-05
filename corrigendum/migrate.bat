rmdir /S /Q main\migrations
rm db.sqlite3
manage.py makemigrations main
manage.py migrate
manage.py createsuperuser
manage.py runserver