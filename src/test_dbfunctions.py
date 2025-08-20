import os
from db import add_habit, get_completions, get_habit_id, get_habits,init_db, mark_done, show_grid, show_streak
import unittest


TEST_DB = "test_habits.db"

if os.path.exists(TEST_DB):
    os.remove(TEST_DB)
    
init_db(TEST_DB)
class TestFunctions(unittest.TestCase):
    def test_addhabit(self):
    
        msg1 = add_habit("Read", TEST_DB)
        self.assertEqual(msg1,"Habit added Successfully\n")
        msg2 = add_habit("Read", TEST_DB)
        self.assertEqual(msg2, "*Habit already exists*\n")

    def test_markdone(self):
        habit_id = 1

        msg1 = mark_done(habit_id, TEST_DB)
        self.assertEqual(msg1, "Habit marked Successfully\n")
        msg2 = mark_done(habit_id, TEST_DB)
        self.assertEqual(msg2, "*Habit already marked*\n")
        print(get_habits(TEST_DB))
        print(get_completions(habit_id, TEST_DB))

    def test_gridstreak(self):
        habit = "Read"
        id = get_habit_id(habit)
        msg1 = mark_done(id, TEST_DB)
        self.assertEqual(msg1, "Habit marked Successfully\n")
        show_grid(id)
        show_streak(id)
              

if __name__ == "__main__":
    unittest.main()