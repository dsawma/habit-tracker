import os
from db import add_habit, get_completions, get_habits,init_db, mark_done
import unittest


TEST_DB = "test_habits.db"

if os.path.exists(TEST_DB):
    os.remove(TEST_DB)
    
init_db(TEST_DB)
class TestFunctions(unittest.TestCase):
    def test_addhabit(self):
    
        msg1 = add_habit("Read", TEST_DB)
        self.assertEqual(msg1,"Habit added Successfully")
        msg2 = add_habit("Read", TEST_DB)
        self.assertEqual(msg2, "Habit already exists")

    def test_markdone(self):
        habit_id = 1
        date = "2025-08-19"

        msg1 = mark_done(habit_id, date, TEST_DB)
        self.assertEqual(msg1, "Habit marked Successfully")
        msg2 = mark_done(habit_id, date, TEST_DB)
        self.assertEqual(msg2, "Habit already marked")
        print(get_habits(TEST_DB))
        print(get_completions(habit_id, TEST_DB))
              

if __name__ == "__main__":
    unittest.main()