# Database Design E-commerce Project
Project source code for Database Design
<br><br>

## Installation Guide
--------------------------
***Note:** Python version >=3.10 is required to install and run the project.

All dependencies for the project are included in the `requirements.txt` file and can be directly installed using the command:

`pip install -r requirements.txt`

## Application Settings
-------------------------
The settings for this project can be found in the file `amazonia/settings.py`.

In this file, the `DATABASES` variable defines the current database in use. The parameters to correctly connect to the database are present in this dictionary. You might need to update the `username` and `password` values in order to connect to your local database with the correct user.

## Setting up the Application
--------------------------
For setting up the application for the first time, run the following commands in order:

1. `python3 manage.py makemigrations` - This command creates sql commands based on the models defined within the application. This reduces the task of defining the sql commands for our tables and makes migration to the database easy.
2. `python3 manage.py migrate` - This command generates the tables in the selected database based on the migration commands created in the previous command.

**Important:** The above commands only create/update the table structure in the database. If you want to manually insert data into the database, either insert it directly or use the Insert sql files provided along with the code.

## Running the Application
--------------------------
To run the application, simply run the command `python3 manage.py runserver`.

By default, the application must run on `localhost:8000` or `127.0.0.1:8000`