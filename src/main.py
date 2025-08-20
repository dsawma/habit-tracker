from db import add_habit, get_habit_id, init_db, mark_done, show_grid, show_streak

def main():
    init_db()
    run = True
    
    while(run):
        print("================")
        print("Habit Tracker")
        print("================")
        print("1. Add a new Habit")
        print("2. Mark a Habit as done")
        print("3. Show Habit grid")
        print("4. Show streak")
        print("5. Exit")
        val = input("Pick an option: ")

        if val == "1":
            print()
            ans = input("Please enter name of habit to add: ")
            print(add_habit(ans,))
        elif val == "2":
            print()
            ans = input("Please enter name of habit to mark: ")
            id = get_habit_id(ans,)
            if id is not None:
                print(mark_done(id,))
            else:
                print("The Habit doesn't exist\n")

        elif val == "3":
            print()
            ans = input("Please enter name of habit: ")
            id = get_habit_id(ans)
            if id is not None:
                show_grid(id,)
            else:
                print("The Habit doesn't exist\n")

        elif val == "4":
            print()
            ans = input("Please enter name of habit: ")
            id = get_habit_id(ans)
            if id is not None:
                show_streak(id,)
            else:
                print("The Habit doesn't exist\n")
        elif val == "5":
            print()
            run = False
        else:
            print()
            print("Invalid option\n")

    print("Goodbye!")


if __name__ == "__main__":
    main()
    