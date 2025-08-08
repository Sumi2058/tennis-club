migration:
	python3 manage.py makemigrations users	

migrate:
	python3 manage.py migrate

run:
	python3 manage.py runserver

db:
	docker run --name postgres -e POSTGRES_USER=root -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=tennis -p 5432:5432 -d postgres:15

project:
	django-admin startproject my_tennis_club

app:
	python3 manage.py startapp users

