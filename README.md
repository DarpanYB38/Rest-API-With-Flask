# Rest-API-With-Flask

# Flask CRUD Application

## Overview

This project is a simple web application built with Flask that allows users to manage a list of items. The application supports basic CRUD (Create, Read, Update, Delete) operations and uses SQLite as the database. SQLAlchemy is used for ORM (Object-Relational Mapping).

## Features

- **Display Items:** View a list of all items stored in the database.
- **Add Items:** Submit a form to add a new item with a name and price.
- **Edit Items:** Modify the details of an existing item.
- **Delete Items:** Remove an item from the list.

## Technologies Used

- **Flask:** A lightweight WSGI web application framework.
- **SQLAlchemy:** ORM for interacting with the SQLite database.
- **SQLite:** Lightweight database for storing item data.

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/DarpanYB38/Rest-API-With-Flask.git
   cd your-repo-name
   ```
## Install Dependencies:
```
  pip install -r requirements.txt

```
## Initialize the Database: 
Run the following commands to create the database and tables 
```
  python
>>> from app import init_db
>>> init_db()
>>> exit()
```
## Run the Application
```
python app.py
```

## Project Structure
- app.py: Main application file with routes and logic.
- templates/: Contains HTML templates.
- items.html: Displays the list of items.
- add_item.html: Form to add a new item.
- edit_item.html: Form to edit an existing item.
- init_db.py: Script to initialize the database (if used separately).

## License
This project is licensed under the MIT License - see the LICENSE file for details.

