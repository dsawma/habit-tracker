import os
from db import add_habit,init_db
import unittest

TEST_DB = "test_habits.db"

if os.path.exists(TEST_DB):
    os.remove(TEST_DB)
    
init_db(TEST_DB)
class TestAddHabit(unittest.TestCase):
    def test_addhabit(self):
    
        msg1 = add_habit("Read", TEST_DB)
        self.assertEqual(msg1,"Habit added Successfully")
        msg2 = add_habit("Read", TEST_DB)
        self.assertEqual(msg2, "Habit already exists")


if __name__ == "__main__":
    unittest.main()