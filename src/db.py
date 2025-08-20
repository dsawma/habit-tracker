import sqlite3
from datetime import date, datetime, timedelta


def init_db(db_name = "habits.db"):
    
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS habits(
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE
        );
        """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS completions (
        id INTEGER PRIMARY KEY,
        habit_id INTEGER,
        date TEXT,
        UNIQUE(habit_id, date),
        FOREIGN KEY(habit_id) REFERENCES habits (id) ON DELETE CASCADE    
              
        );
        """)
        connection.commit()

def add_habit(name, db_name = "habits.db"):
    try : 
        with  sqlite3.connect(db_name) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO habits (name) VALUES (?)", (name,))
            connection.commit()
        return "Habit added Successfully\n"
    except sqlite3.IntegrityError:
        return "*Habit already exists*\n"

def mark_done(id, db_name="habits.db"):
    try : 
        with  sqlite3.connect(db_name) as connection:
            today_date = date.today().strftime("%Y-%m-%d")
            cursor = connection.cursor()
            cursor.execute("INSERT INTO completions (habit_id, date) VALUES (?,?)", (id,today_date))
            connection.commit()
        return "Habit marked Successfully\n"
    except sqlite3.IntegrityError:
        return "*Habit already marked*\n"

def get_habits(db_name="habits.db"):
    
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, name FROM habits ORDER BY name")
        habits = cursor.fetchall()
    return habits 

def get_habit_id(name, db_name="habits.db"):
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, name FROM habits WHERE name = ?",(name,) )
        habit = cursor.fetchone()
        if habit:
            return habit[0]
        else:
            return None

def get_completions(habit_id, db_name="habits.db"):
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT date FROM completions WHERE habit_id = ? ORDER BY date", (habit_id,))
        completions = [row[0] for row in cursor.fetchall()]
    return completions

def show_grid(habit_id, db_name = "habits.db"):
    # converts strings of dates to days objects and places them in a list
    completion_dates = [datetime.strptime(d,"%Y-%m-%d").date() for d in get_completions(habit_id)]
    today_date = date.today()
    start_date = today_date - timedelta(days =83)
    # sequential 84 dates for 7 x 12 grid 
    all_days= []
    completion_set = set(completion_dates)
    for i in range(84):
        day = start_date + timedelta(days =i)
        all_days.append(day)
    day_count = 0

    for day in all_days:
        if day_count == 7:
            print("\n")
            day_count =0
        if day in completion_set:
            print("■", end=" ")
        else:
            print(".", end=" ")
        day_count += 1
    print("\n")

def show_streak(habit_id, db_name = "habits.db"):
    completion_dates = [datetime.strptime(d,"%Y-%m-%d").date() for d in get_completions(habit_id)]
        
    current_streak = 0
    longest_streak = 0
    previous_day = None
    for day in completion_dates:
        if previous_day is not None and day == previous_day + timedelta(days =1):
            current_streak += 1
        else:
            current_streak = 1
        if current_streak > longest_streak:
            longest_streak = current_streak
        previous_day = day
    print(f"Longest Streak: {longest_streak}")
    print(f"Current Streak: {current_streak}")
   







