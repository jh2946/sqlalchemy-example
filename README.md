# sqlalchemy-example

## Introduction to Flask-SQLAlchemy

This tutorial will only assume knowledge of Python up to classes and objects for chapters 1-4, though knowledge of Shelve will be beneficial for comparison purposes. For chapters 5-6, knowledge of basic Flask requests and WTForms will also be required.

Relational databases store data as tables instead of objects. A `Person` table, for example, stores each person as a row. Each column of the row describes one thing about the person (for example, their name, their email). Very importantly, one row must represent one real-life object or relationship. It can be a person and contain their name and email. It can be a purchase and contain the customer ID and the total price. It can even be a parent-child relationship and contain the NRICs of the parent and the child.

In the industry, tables are known for their data integrity and removal of redundancy. For those doing the application project, this might appeal to you: tables reduce tasks such as "List the emails of all employees in the logistics department" to a single-line query. Without tables, you would have to go to the dictionary of employees (which may be hidden away in Sh\*lve 🤮 or whatever), write a for loop and check if each employee's department is "logistics". (By the way, SQLite is a relational database, while Sh\*lve 🤮 is a key-value database.)

Flask-SQLAlchemy allows us to view tables as classes and objects. Each Python class is one table, each Python object is one row, and each class attribute is one column. It's a fairly elegant, intuitive mapping to whatever we've been taught so far about Python classes and objects.

The hardest part of learning Flask-SQLAlchemy is probably creating quality table structures (schemas), which can be more complicated than writing the code itself. Some may also find the querying methods quite challenging, and resort back to for loops and if statements, which gets the job done but defeats the whole purpose of Flask-SQLAlchemy.

## Repository introduction

The prerequisite tools you'll need are:

- Git (my version: 2.39.0.windows.2)
- Python >=3.7 (my version: 3.11.4; ensure `pip` is in environment variables as you'll need to call it in terminal)

There are several `Ex-` folders in this repository. Each has the general structure:

```
Ex-0-Example
├───app
│   ├───__init__.py
│   └───models.py
├───main.py
└───README.md
```

- `app/__init__.py` contains the boilerplate code. You can generally ignore this file.

- `app/models.py` contains the database models, which you will be editing.

- `main.py` contains application logic, which you will be editing.

- `README.md` contains the tutorial content. It's recommended to read this on GitHub on your browser.

There's a `Console-Workspace` directory with a similar structure which already contains boilerplate code, and is meant for your tinkering.

If you have any issues feel free to drop it in the Issues section of this repo.

## Setup

### VSCode

Open a new terminal in VSCode and run the following:

```
git clone https://github.com/jh2946/sqlalchemy-example .
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```

You will have to run `venv/Scripts/activate` in this root directory every time you open this folder.

If you want to avoid activating `venv` every time you open this repository, do `Ctrl+Shift+P`, type "Preferences: Open User Settings (JSON)", and paste the following inside the outer braces at the start (must Ctrl+S after this):

```json
    "python.terminal.activateEnvInCurrentTerminal": true,
    "python.defaultInterpreterPath": "~/venv/Scripts/python.exe",
```

Run `main.py` for each chapter.

### PyCharm

```
git clone https://github.com/jh2946/sqlalchemy-example
cd sqlalchemy-example
pip install -r requirements.txt
```

Run `main.py` for each chapter.
