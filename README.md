CREATE PostgreSQL
----
1. Create user and DB in PostgreSQL
         
         sudo su postgres
         psql
         CREATE USER admin42 WITH PASSWORD '123456' CREATEDB;
         CREATE DATABASE postDB OWNER admin42;
         GRANT ALL PRIVILEGES ON DATABASE postDB TO admin42;
         exit



         DATABASES = {
             "default": {
                 "ENGINE": "django.db.backends.postgresql",
                 "NAME": "blogdb",
                 "USER": "admin44",
                 "PASSWORD": "123456",
                 "HOST": "localhost",
                 "PORT": 5432,
             }
         }
         


2. Requirements.txt
         
         pip install -r requirements.txt  
         pip freeze > requirements.txt


3. Create new "blog"

         python manage.py startapp blog

4. Createsuperuser
         
         python manage.py createsuperuser

5. Create  migrations

         python manage.py makemigrations
         python manage.py migrate