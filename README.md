# sqlalchemy-example

## Repository introduction

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

## Setup

If you're on VSCode, run the following in a new folder using VSCode Terminal:

```
git clone https://github.com/jh2946/sqlalchemy-example .
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```

You will have to run `venv/Scripts/activate` in this root directory every time you open this folder.

Then just `cd` into each folder to view each working example, and run `python main.py`.
