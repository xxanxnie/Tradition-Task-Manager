# Task Manager (Traditional Coding Approach)

This is a simple task management application built using the traditional software development stack: **Python (Flask)** for the backend, **SQLite** for the database, and **HTML/CSS/JavaScript** for the frontend. It demonstrates how to manually build a full-stack web app without low-code/no-code tools.

## Features
- Task creation, editing, and deletion
- Task categorization and due date assignment
- Reporting: Completed vs. pending tasks
- Data persistence with SQLite
- Asynchronous task creation/deletion via AJAX

## Installation & Running the App
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

python3 setup_db.py
python3 app.py
Running on http://127.0.0.1:5000