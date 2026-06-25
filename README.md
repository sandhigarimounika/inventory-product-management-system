# Inventory Product Management System

## Project Overview

The Inventory Product Management System is a web-based application developed using Django and Django REST Framework. It helps users manage inventory products efficiently by providing Create, Read, Update, and Delete (CRUD) operations.

## Features

* Add new products
* View all products
* View product details
* Update product information
* Delete products
* REST API integration
* SQLite database support

## Technologies Used

* Python
* Django
* Django REST Framework
* SQLite
* HTML

## Project Structure

* models.py – Defines database tables
* views.py – Handles business logic
* urls.py – Defines URL routing
* serializer.py – Converts data to JSON format
* templates/ – Contains HTML pages

## API Endpoints

* GET /api/products/
* POST /api/products/
* GET /api/products/<id>/
* PUT /api/products/<id>/
* DELETE /api/products/<id>/

## How to Run

1. Install dependencies
2. Run migrations
3. Start the server

Commands:

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

## Author

Mounika
