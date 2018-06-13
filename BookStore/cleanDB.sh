rm db.sqlite3;
rm BookDetails/migrations/0* ;

python manage.py makemigrations;
python manage.py migrate
