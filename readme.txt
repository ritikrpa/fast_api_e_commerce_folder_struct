---

FastAPI E-Commerce Backend

A clean, scalable FastAPI project using MySQL, SQLAlchemy, and layered architecture.

---

Tech Stack

* FastAPI
* MySQL
* SQLAlchemy
* Pydantic
* Uvicorn

---

Prerequisites

* Python 3.10 or higher (tested on 3.14.3)
* Homebrew (for macOS)
* MySQL Server

---

Setup Instructions

1. Verify Python

Run:
python3 --version

Note:
Use "python3" instead of "python" on macOS.

---

2. Create Virtual Environment

Run:
python3 -m venv .venv

---

3. Activate Virtual Environment

Run:
source .venv/bin/activate

You should see (.venv) in your terminal.

---

4. Install Dependencies

If requirements.txt exists:

pip install -r requirements.txt

If not:

pip install fastapi uvicorn sqlalchemy pymysql python-dotenv
pip freeze > requirements.txt

---

MySQL Setup (macOS)

1. Install MySQL

brew install mysql

2. Start MySQL Service

brew services start mysql

3. Login to MySQL

mysql -u root -p

Press Enter if no password is set.

4. Create Database

CREATE DATABASE ecommerce_db;

5. Verify Database

SHOW DATABASES;

6. Exit

exit;

---

Environment Variables

Create a .env file in the project root and add:

DB_URL=mysql+pymysql://root:password@localhost/ecommerce_db

Replace "password" if your MySQL has one.

If no password is set, use:
mysql+pymysql://root@localhost/ecommerce_db

---

Run the Server

uvicorn app.main:app --reload

---

API Documentation

Swagger UI:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

ReDoc:
[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

Project Structure

app/
api/
core/
models/
schemas/
repositories/
services/
utils/

---

Important Notes

* Always activate the virtual environment before running the project.
* Ensure MySQL is running before starting the server.
* The database must be created manually before running FastAPI.
* The .venv folder should not be committed to version control.
* The .env file should not be committed (it may contain sensitive data).

---
