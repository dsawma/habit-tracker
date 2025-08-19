import sqlite3

def init_db(db_name = "habits.db"):
    connection = sqlite3.connect("habits.db")
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS habits(
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE
    );
    """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS completions (
    id INTEGER PRIMARY KEY,
    habit_id INTEGER,
    date TEXT
    );
    """)
    connection.commit
    connection.close

def add_habit(name, db_name = "habits.db"):
    try : 
        with  sqlite3.connect("habits.db") as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO habits (name) VALUES (?)", (name,))
            connection.commit
        return "Habit added Successfully"
    except sqlite3.IntegrityError:
        return "Habit already exists"
    
    



